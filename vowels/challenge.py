import sys


total_vowels = {
	'a': 0,
	'e': 0,
	'i': 0,
	'o': 0,
	'u': 0
}

def print_counts(vowels):
	print()
	for vowel, count in vowels.items():
		print("{}: {}".format(vowel, count))

def count_vowels(user_input):
	vowels = {
		'a': 0,
		'e': 0,
		'i': 0,
		'o': 0,
		'u': 0
	}
	for char in user_input:
		if char in ('a', 'A'):
			vowels['a'] += 1
			total_vowels['a'] += 1
		elif char in ('e', 'E'):
			vowels['e'] += 1
			total_vowels['e'] += 1
		elif char in ('i', 'I'):
			vowels['i'] += 1
			total_vowels['i'] += 1
		elif char in ('o', 'O'):
			vowels['o'] += 1
			total_vowels['o'] += 1
		elif char in ('u', 'U'):
			vowels['u'] += 1
			total_vowels['u'] += 1
	return vowels


def main():
	done = False
	while not done:
		print("Please enter sentence: ")
		try:
			user_input = input()
		except KeyboardInterrupt:
			print_counts(total_vowels)
			sys.exit()
		else:
			vowels = count_vowels(user_input)
			print_counts(vowels)


if __name__ == "__main__":
	main()
