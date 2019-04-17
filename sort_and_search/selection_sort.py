def selection_sort(numbers):
	"""Return sorted list using selection sort algorithm"""
	for index, number in enumerate(numbers[:-1]):
		min_index = index
		for compare_index, compare_number in enumerate(numbers[index+1:], index+1):
			if compare_number < numbers[min_index]:
				min_index = compare_index

		min_value = numbers[min_index]
		temp = numbers[index]
		numbers[index] = min_value
		numbers[min_index] = temp

	return numbers
