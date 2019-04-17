def insertion_sort(input_list):
	for index in range(1, len(input_list)):
		current_value = input_list[index]
		position = index
		while position > 0 and input_list[position - 1] > current_value:
			input_list[position] = input_list[position - 1]
			position -= 1
		input_list[position] = current_value
	return input_list


def binary_search(sorted_list, target):
	low = 0
	high = len(sorted_list) - 1
	while low <= high:
		mid = (low + high) // 2
		mid_value = sorted_list[mid]
		if mid_value == target:
			return True
		elif mid_value < target:
			low = mid + 1
		elif mid_value > target:
			high = mid - 1
	return False


sorted_list = insertion_sort([5, 10, 2, 9, 7])
found_value = binary_search(sorted_list, 8)
