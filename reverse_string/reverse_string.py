def reverse_string(word):
    """Reverse the letters in a word."""
    forward = []
    for letter in word:
        forward.append(letter)
    reverse = []
    for letter in forward:
        reverse.insert(0, letter)
    reverse = ''.join(reverse)
    return reverse
