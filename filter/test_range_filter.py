import pytest
import numpy as np
from range_filter import RangeFilter


@pytest.fixture()
def range_filter():
	return RangeFilter(0.03, 50)

def test_update_range_min_filter(range_filter):
	input_scan = np.array([0, 0.01, 0.025, 0.03, 0.031, 0.4 ])
	update_scan = range_filter.update(input_scan)
	expected_output = np.array([0.03, 0.03, 0.03, 0.03, 0.031, 0.4])
	assert np.array_equal(update_scan, expected_output) == True

def test_update_range_max_filter(range_filter):
	input_scan = np.array([10, 45, 50, 51, 75, 100])
	update_scan = range_filter.update(input_scan)
	expected_output = np.array([10, 45, 50, 50, 50, 50])
	assert np.array_equal(update_scan, expected_output) == True

def test_update_range_min_and_max_filter(range_filter):
	input_scan = np.array([0, 0.01, 0.03, 45, 50, 51])
	update_scan = range_filter.update(input_scan)
	expected_output = np.array([0.03, 0.03, 0.03, 45, 50, 50])
	assert np.array_equal(update_scan, expected_output) == True
