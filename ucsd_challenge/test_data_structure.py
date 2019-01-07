from data_structure import DataStructure

def test_insert_default_constructor():
	ds = DataStructure()
	ds.insert(1)
	assert len(ds.values) == 1

def test_insert_specifying_initial_values():
	ds = DataStructure([1, 2, 3, 4, 5])
	ds.insert(6)
	assert len(ds.values) == 6

def test_remove_single_value():
	ds = DataStructure([1, 2, 3, 4, 5])
	ds.remove(5)
	assert 5 not in ds.values

def test_remove_multiple_duplicate_values():
	ds = DataStructure([1, 5, 2, 5, 3, 4, 5])
	ds.remove(5)
	assert 5 not in ds.values

def test_get_random_in_appropriate_range():
	ds = DataStructure([1, 5, 2, 5, 3, 4, 5])
	output = ds.get_random()
	assert output >= 1 and output <= 5
