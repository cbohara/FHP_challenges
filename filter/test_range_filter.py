import pytest
import numpy as np
from range_filter import RangeFilter

@pytest.fixture()
def range_filter():
	return RangeFilter(0.03, 50)

def test_update_for_range_min_filter(range_filter, input_scans):
	filtered_scans = range_filter.update(u
	expected_output = np.array([0.03, 0.03, 0.03, 0.03, 0.031, 0.4])
	assert np.array_equal(filtered_scans, expected_output) == True

def test_update_for_range_max_filter(range_filter, input_scans):
	filtered_scans = range_filter.update([10, 45, 50, 51, 75, 100])
	assert filtered_scans == [10, 45, 50, 50, 50, 50]

def test_update_for_range_min_and_max_filter(range_filter, input_scans):
	filtered_scans = range_filter.update([0, 0.01, 0.03, 45, 50, 51])
	assert filtered_scans == [0.03, 0.03, 0.03, 45, 50, 50]
