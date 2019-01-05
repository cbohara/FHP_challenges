from selection_sort import selection_sort

def test_selection_sort_numbers():
	unsorted = [2, 0, 11, 12, 13, -1]
	assert selection_sort(unsorted) == [-1, 0, 2, 11, 12, 13]

def test_selection_sort_letters():
	unsorted = ['b', 'c', 'a', 'd']
	assert selection_sort(unsorted) == ['a', 'b', 'c', 'd']
