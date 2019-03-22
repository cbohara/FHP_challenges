import sys
import os
import json
import requests
from datetime import date, datetime, timedelta
from pymysql import cursors, connect


def load_api_data(config, page_number):
	"""Load API data from external provider"""
	api_endpoint = config.api_endpoint
	api_version = config.api_version
	url = api_endpoint.format(api_version, page_number)
	json_data = requests.get(url).text
	dict_data = json.loads(json_data)
	return dict_data

def get_ext_users(config, page_number):
	"""Get list of external user dictionaries"""
	dict_data = load_api_data(config, page_number)
	return dict_data["users"]

def query_mysql(config, sql):
	"""Query internal MySQL table"""
	connection = connect(
		host=config.db_host,
		user=config.db_user,
		password=config.db_password,
		port=config.db_port,
		db=config.db_schema,
		cursorclass=cursors.DictCursor
	)
	try:
		with connection.cursor() as cursor:
			cursor.execute(sql)
			result = cursor.fetchall()
	finally:
		connection.close()
	return result

def get_total_int_users(config):
	"""Get total number of internal users"""
	sql = """SELECT count(*)
			FROM user
			JOIN user_practice ON user.practice_id = user_practice.id"""
	return query_mysql(config, sql)[0]["count(*)"]

def get_int_users(config, start_lastname, end_lastname):
	"""Get list of internal user dictionaries"""
	sql = """SELECT user.id AS id, firstname, lastname, specialty, last_active_date, location
			FROM user
			JOIN user_practice ON user.practice_id = user_practice.id
			WHERE lastname BETWEEN "{}" and "{}"
			ORDER BY lastname
			""".format(start_lastname, end_lastname)
	int_users = query_mysql(config, sql)
	return int_users

def is_user_match(int_user, ext_user):
	"""Determine if the internal and external user are the same user"""
	required_match_fields = ("lastname", "firstname", "location", "specialty")
	for field in required_match_fields:
		if int_user[field] != ext_user[field]:
			return False
	return True

def get_user_active_status(config, current_date, user):
	"""Determine if the user is currently active"""
	day_delta = current_date - user["last_active_date"]
	if day_delta < timedelta(days=int(config.active_day_range)):
		return "active"
	else:
		return "inactive"

def are_both_active_users(int_user, ext_user):
	"""Determine if both internal and external user are active"""
	if (int_user["int_active_status"] == "active") and (ext_user["ext_active_status"] == "active"):
		return True
	else:
		return False

def normalize_and_augment_ext_user(config, current_date, ext_user):
	"""Normalize external user data and augment with API ID, version, and active status"""
	ext_user["last_active_date"] = datetime.strptime(ext_user["last_active_date"], "%Y-%m-%d").date()
	ext_user["ext_active_status"] = get_user_active_status(config, current_date, ext_user)

	ext_user["location"] = ext_user["practice_location"].replace("_", " ")
	del ext_user["practice_location"]

	ext_user["ext_classification"] = ext_user["user_type_classification"]
	del ext_user["user_type_classification"]

	ext_user["api_id"] = ext_user["id"]
	del ext_user["id"]
	ext_user["api_version"] = config.api_version
	return ext_user

def get_warehouse_row(int_user, ext_user):
	"""Get rows that would be loaded to the warehouse"""
	row = ext_user
	row["ext_last_active_date"] = ext_user["last_active_date"]
	del row["last_active_date"]
	row["int_last_active_date"] = int_user["last_active_date"]
	row["user_id"]= int_user["id"]
	row["int_active_status"] = int_user["int_active_status"]
	return row

def compare_users(config, current_date, ext_users, int_users):
	"""Compare internal and external users and return active user match count and warehouse database fields"""
	active_user_matches = 0
	rows = []
	for ext_user in ext_users:
		ext_user = normalize_and_augment_ext_user(config, current_date, ext_user)

		for index, int_user in enumerate(int_users):
			if is_user_match(int_user, ext_user):
				int_user["int_active_status"] = get_user_active_status(config, current_date, int_user)
				row = get_warehouse_row(int_user, ext_user)
				rows.append(row)

				if are_both_active_users(int_user, ext_user):
					active_user_matches += 1
				del int_users[index]
				break
	return (active_user_matches, rows)

def setup(config):
	"""Initialize variables"""
	if not config.current_date:
		current_date = date.today()
	else:
		current_date = datetime.strptime(config.current_date, "%Y-%m-%d").date()

	if not config.api_pages:
		total_pages = load_api_data(config, 1)["total_pages"]
	else:
		total_pages = config.api_pages

	start_time = datetime.now()
	return (start_time, current_date, total_pages)

def print_page_stats(page, ext_users, int_users, active_matches):
	"""Print stats per API page comparison for logging purposes"""
	print("page: {} ext_users: {} int_users: {} active_matches: {}".format(page, len(ext_users), len(int_users), active_matches))
	sys.stdout.flush()

def print_total_counts(config, total_ext_users, total_active_matches):
	"""Print total counts"""
	total_int_users = get_total_int_users(config)
	print("total external users: {}".format(total_ext_users))
	print("total internal users: {}".format(total_int_users))
	print("total active matches: {}".format(total_active_matches))

def get_elapsed_time(start_time):
	"""Get elapsed time to run script"""
	total_seconds = (datetime.now() - start_time).seconds
	minutes, seconds = divmod(total_seconds, 60)
	if minutes > 0:
		return "elapsed time: {} minutes, {} seconds".format(minutes, seconds)
	else:
		return "elapsed time: {} seconds".format(seconds)

def get_json_rep_of_sample_rows(config, warehouse_rows):
	"""Get sample warehouse rows output"""
	sample_rows = warehouse_rows[:int(config.sample_rows)]
	return json.dumps(sample_rows, indent=4, default=str)

def get_sql_ddl():
	return """CREATE TABLE active_match(
				id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
				firstname VARCHAR(50),
				lastname VARCHAR(50),
				specialty VARCHAR(50),
				location VARCHAR(50),
				ext_classification VARCHAR(50),
				api_id INT(11),
				api_version VARCHAR(50),
				ext_last_active_date DATE,
				int_last_active_date DATE,
				int_active_status VARCHAR(50),
				ext_active_status VARCHAR(50),
				user_id INT(11),
				FOREIGN KEY fk_cat(user_id)
				REFERENCES user(id)
			);"""

def write_output(config, elapsed_time, total_active_matches, warehouse_rows):
	"""Write expected output per requirements"""
	sql_ddl = get_sql_ddl()
	sample_rows = get_json_rep_of_sample_rows(config, warehouse_rows)
	with open("output.txt", "w") as f:
		f.write(elapsed_time + "\n\n")
		f.write("total active matches: {}\n\n".format(total_active_matches))
		f.write("sample output: \n")
		f.write(sample_rows + "\n\n")
		f.write("SQL DDL: \n")
		f.write(sql_ddl)

def execute(config):
	start_time, current_date, total_pages = setup(config)

	total_active_matches = 0
	total_ext_users = 0
	warehouse_rows = []
	for page in range(1, total_pages+1):
		ext_users = get_ext_users(config, page)
		total_ext_users += len(ext_users)

		int_users = get_int_users(config, ext_users[0]["lastname"], ext_users[-1]["lastname"])

		active_matches, rows = compare_users(config, current_date, ext_users, int_users)
		total_active_matches += active_matches
		warehouse_rows += rows

		print_page_stats(page, ext_users, int_users, active_matches)

	print_total_counts(config, total_ext_users, total_active_matches)
	elapsed_time = get_elapsed_time(start_time)

	write_output(config, elapsed_time, total_active_matches, warehouse_rows)

if __name__ == "__main__":
	import configargparse
	config_parser = configargparse.ArgParser()
	config_parser.add('-c', '--config-file', required=False, is_config_file=True, help='config file path')
	config_parser.add('--current_date', help='YYYY-MM-DD format defaults to current date')
	config_parser.add('--active_day_range', required=True, help='user is considered active if last_active_date with x days')
	config_parser.add('--api_version', required=True, help='external partner API endpoint')
	config_parser.add('--api_endpoint', required=True, help='external partner API endpoint')
	config_parser.add('--api_pages', required=False, type=int, help='total API pages to load')
	config_parser.add('--db_host', required=True, help='internal mysql database host')
	config_parser.add('--db_user', required=True, help='internal mysql database user')
	config_parser.add('--db_password', required=True, help='internal mysql database password')
	config_parser.add('--db_port', required=True, type=int, help='internal mysql database port')
	config_parser.add('--db_schema', required=True, help='internal mysql database schema')
	config_parser.add('--sample_rows', type=int, default=10, help='number of sample warehouse rows to print to output file')

	config = config_parser.parse_args()
	for key, value in vars(config).items():
		print('{} = {}'.format(key, value))

	execute(config)
