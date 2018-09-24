import pytest
from collections import deque
from ring_buffer import RingBuffer


def test_initialize_full_queue():
	ring_buffer = RingBuffer([x for x in range(5)], 5)
	expected_queue = deque([x for x in range(5)], 5)
	assert ring_buffer.queue == expected_queue

def test_initialize_empty_queue():
	ring_buffer = RingBuffer([], 5)
	expected_queue = deque([], 5)
	assert ring_buffer.queue == expected_queue

def test_add_value_to_not_full_queue():
	ring_buffer = RingBuffer([x for x in range(3)], 5)
	ring_buffer.add_value(2)
	assert len(ring_buffer.queue) == 4

def test_add_value_to_full_queue_removes_first_value_and_adds_new_value():
	ring_buffer = RingBuffer([x for x in range(5)], 5)
	ring_buffer.add_value(10)
	expected_queue = deque([1, 2, 3, 4, 10])
	assert ring_buffer.queue == expected_queue

def test_add_values_to_full_queue_removes_first_two_values_and_adds_two_new_values():
	ring_buffer = RingBuffer([x for x in range(5)], 5)
	ring_buffer.add_values([10, 100])
	expected_queue = deque([2, 3, 4, 10, 100])
	assert ring_buffer.queue == expected_queue

def test_add_values_replaces_entire_queue():
	ring_buffer = RingBuffer([x for x in range(5)], 5)
	ring_buffer.add_values([
		x
		for x in range(50)
		if x % 10 == 0
	])
	expected_queue = deque([0, 10, 20, 30, 40])
	assert ring_buffer.queue == expected_queue

def test_add_values_replaces_newest_values():
	ring_buffer = RingBuffer([x for x in range(5)], 5)
	ring_buffer.add_values([
		x
		for x in range(100)
		if x % 10 == 0
	])
	expected_queue = deque([50, 60, 70, 80, 90])
	assert ring_buffer.queue == expected_queue
