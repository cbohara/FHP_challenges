from linear_search import linear_search

def test_linear_search_find_target():
	iterable = ["apple", "grape", "orange"]
	assert linear_search(iterable, "grape") == True

def test_linear_search_did_not_find_target():
	iterable = ["apple", "grape", "orange"]
	assert linear_search(iterable, "banana") == False
