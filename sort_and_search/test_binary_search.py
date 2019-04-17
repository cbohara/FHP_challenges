from binary_search import binary_search

def test_binary_search_found_target():
	iterable = range(5)
	assert binary_search(iterable, 2) == True

def test_binary_search_did_not_target_greater_than_range():
	iterable = range(5)
	assert binary_search(iterable, 10) == False

def test_binary_search_did_not_target_less_than_range():
	iterable = range(1, 5)
	assert binary_search(iterable, 0) == False

def test_binary_search_did_not_target_within_range():
	iterable = [x for x in range(0, 12) if x % 3 == 0]
	assert binary_search(iterable, 2) == False
