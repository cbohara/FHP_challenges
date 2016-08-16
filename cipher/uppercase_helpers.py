def upper_list():
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return upper

def upper_index(char):
    """Returns the index of the char in the list of uppercase letters."""
    upper = upper_list()
    for index, value in enumerate(upper):
        if char == value:
            return index

def upper_char(index):
    """Returns the char at the input index in the upper_list."""
    upper = upper_list()
    upper += upper[0:13]
    return upper[index]
