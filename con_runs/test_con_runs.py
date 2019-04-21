from con_runs import con_runs

def test_empty_input_list():
	assert con_runs([]) == None

def test_len_input_list_less_than_con_value():
	assert con_runs([1, 2]) == None

def test_len_input_list_equals_con_value_positive_inc():
	assert con_runs([1, 2, 3]) == [0]

def test_len_input_list_equals_con_value_neg_inc():
	assert con_runs([-1, -2, -3]) == [0]

def test_len_input_list_equals_con_value_no_inc():
	assert con_runs([-1, 5, 2]) == None

def test_len_input_list_greater_con_value_simple_inc():
	assert con_runs([1, 2, 3, 4, 5, 6, 7]) == [0, 1, 2, 3, 4]

def test_len_input_list_greater_con_value_varied_inc():
	assert con_runs([5, 2, 3, 4, 9, 10, 11]) == [1, 4]

def test_len_input_list_greater_con_value_single_dec():
	assert con_runs([5, 8, -3, -4, -5, 10, 11]) == [2]

def test_len_input_list_greater_con_value_varied_inc_and_dec():
	assert con_runs([1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]) == [0, 4, 6, 7]

def test_len_input_list_greater_con_value_no_inc_or_dec():
	assert con_runs([-10, 11, -7, 8, 7]) == None
