import pytest
import numpy as np
from temporal_median_filter import TemporalMedianFilter

@pytest.fixture()
def temporal_median_filter():
	return TemporalMedianFilter(3)

@pytest.fixture()
def input_scans():
	return [
		np.array([0.0, 1.0, 2.0, 1.0, 3.0]),
		np.array([1.0, 5.0, 7.0, 1.0, 3.0]),
		np.array([2.0, 3.0, 4.0, 1.0, 0.0]),
		np.array([3.0, 3.0, 3.0, 1.0, 3.0]),
		np.array([10.0, 2.0, 4.0, 0.0, 0.0])
	]

def test_update_time0(temporal_median_filter, input_scans):
	update_scan = temporal_median_filter.update(input_scans[0])
	expected_output = np.array([0.0, 1.0, 2.0, 1.0, 3.0])
	assert np.array_equal(update_scan, expected_output) == True

def test_update_time0_to_time1(temporal_median_filter, input_scans):
	for scan in input_scans[:2]:
		update_scan = temporal_median_filter.update(scan)
	expected_output = np.array([0.5, 3.0, 4.5, 1.0, 3.0])
	assert np.array_equal(update_scan, expected_output) == True

def test_update_time0_to_time2(temporal_median_filter, input_scans):
	for scan in input_scans[:3]:
		update_scan = temporal_median_filter.update(scan)
	expected_output = np.array([1.0, 3.0, 4.0, 1.0, 3.0])
	assert np.array_equal(update_scan, expected_output) == True

def test_update_time0_to_time3(temporal_median_filter, input_scans):
	for scan in input_scans[:4]:
		update_scan = temporal_median_filter.update(scan)
	expected_output = np.array([1.5, 3.0, 3.5, 1.0, 3.0])
	assert np.array_equal(update_scan, expected_output) == True

def test_update_time0_to_time4(temporal_median_filter, input_scans):
	for scan in input_scans[:5]:
		update_scan = temporal_median_filter.update(scan)
	expected_output = np.array([2.5, 3.0, 4.0, 1.0, 1.5])
	assert np.array_equal(update_scan, expected_output) == True
