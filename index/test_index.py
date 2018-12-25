import pytest
from index import string_diff_index, list_diff_index

def test_string_diff_index_equal_strings():
	assert string_diff_index("abc", "abc") == -1

def test_string_diff_index_diff_equal_strings():
	assert string_diff_index("abc", "abf") == 2

def test_string_diff_index_unequal_strings_longer_first():
	assert string_diff_index("abcdefg", "abc") == 3

def test_string_diff_index_unequal_strings_longer_second():
	assert string_diff_index("abc", "abcdefg") == 3

def test_list_diff_index_equal_lists():
	list1 = ["abc", "def"]
	list2 = ["abc", "def"]
	assert list_diff_index(list1, list2) == (-1, -1)

def test_list_diff_index_equal_list_len_diff_strings():
	list1 = ["abc", "dbf"]
	list2 = ["abc", "def"]
	assert list_diff_index(list1, list2) == (1, 1)

def test_list_diff_index_equal_list_len_diff_strings():
	list1 = ["azc", "dbf"]
	list2 = ["abc", "def"]
	assert list_diff_index(list1, list2) == (0, 1)

def test_list_diff_index_unequal_list_len_longer_first():
	list1 = ["abc", "def", "ghi"]
	list2 = ["abc", "def"]
	assert list_diff_index(list1, list2) == (2, -1)

def test_list_diff_index_unequal_list_len_longer_first():
	list1 = ["abc", "def", "ghi"]
	list2 = ["abc", "def", "ghi", "lmn"]
	assert list_diff_index(list1, list2) == (3, -1)
