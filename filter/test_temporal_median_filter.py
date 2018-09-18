import pytest
import numpy as np
from temporal_median_filter import TemporalMedianFilter

def test_update_time0():
	temporal_median_filter = TemporalMedianFilter(3)
	time0 = temporal_median_filter.update([0.0, 1.0, 2.0, 1.0, 3.0])
	expected_output = np.array([0.0, 1.0, 2.0, 1.0, 3.0])
	assert np.array_equal(time0, expected_output) == True

def test_update_time1():
	temporal_median_filter = TemporalMedianFilter(3)
	time0 = temporal_median_filter.update([0.0, 1.0, 2.0, 1.0, 3.0])
	time1 = temporal_median_filter.update([1.0, 5.0, 7.0, 1.0, 3.0])
	expected_output = np.array([0.5, 3.0, 4.5, 1.0, 3.0])
	assert np.array_equal(time1, expected_output) == True

def test_update_time2():
	temporal_median_filter = TemporalMedianFilter(3)
	time0 = temporal_median_filter.update([0.0, 1.0, 2.0, 1.0, 3.0])
	time1 = temporal_median_filter.update([1.0, 5.0, 7.0, 1.0, 3.0])
	time2 = temporal_median_filter.update([2.0, 3.0, 4.0, 1.0, 0.0])
	expected_output = np.array([1.0, 3.0, 4.0, 1.0, 3.0])
	assert np.array_equal(time2, expected_output) == True

def test_update_time3():
	temporal_median_filter = TemporalMedianFilter(3)
	time0 = temporal_median_filter.update([0.0, 1.0, 2.0, 1.0, 3.0])
	time1 = temporal_median_filter.update([1.0, 5.0, 7.0, 1.0, 3.0])
	time2 = temporal_median_filter.update([2.0, 3.0, 4.0, 1.0, 0.0])
	time3 = temporal_median_filter.update([3.0, 3.0, 3.0, 1.0, 3.0])
	expected_output = np.array([1.5, 3.0, 3.5, 1.0, 3.0])
	assert np.array_equal(time3, expected_output) == True

def test_update_time4():
	temporal_median_filter = TemporalMedianFilter(3)
	time0 = temporal_median_filter.update([0.0, 1.0, 2.0, 1.0, 3.0])
	time1 = temporal_median_filter.update([1.0, 5.0, 7.0, 1.0, 3.0])
	time2 = temporal_median_filter.update([2.0, 3.0, 4.0, 1.0, 0.0])
	time3 = temporal_median_filter.update([3.0, 3.0, 3.0, 1.0, 3.0])
	time4 = temporal_median_filter.update([10.0, 2.0, 4.0, 0.0, 0.0])
	expected_output = np.array([2.5, 3.0, 4.0, 1.0, 1.5])
	assert np.array_equal(time4, expected_output) == True
