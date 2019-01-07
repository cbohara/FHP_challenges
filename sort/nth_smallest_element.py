def nth_smallest_element(input_list, n):
	"""Get the nth smallest element in a list"""
	deduped_sorted_list = list(sorted(set(input_list)))
	return deduped_sorted_list[n - 1]
