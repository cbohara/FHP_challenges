def lower_list():
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return lower

def lower_index(char):
    """Returns the index of the char in the list of lowercase letters."""
    lower = lower_list()
    for index, value in enumerate(lower):
        if char == value:
            return index

def lower_char(index):
    """Returns the char at the input index in the lower_list."""
    lower = lower_list()
    lower += lower[0:13]
    return lower[index]

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
