def palindrome(string):
    """Returns false for non-palindromes, otherwise returns true."""
    forward = list(string)
    reverse = forward[::-1]
    for forward_char in forward:
        for reverse_char in reverse:
            if forward_char != reverse_char:
                return False
            else:
                return True
    return True


palindrome("hello")
