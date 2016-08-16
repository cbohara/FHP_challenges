import uppercase_helpers as uch
import lowercase_helpers as lch

def rot13(input_string):
    """Rotates each letter in the string by 13 characters, maintaining capitalization and spaces."""
    string = list(input_string)
    output = []
    for char in string:
        if char.isupper():
            index = uch.upper_index(char)
            index += 13
            output.append(uch.upper_char(index))
        elif char.islower():
            index = lch.lower_index(char)
            index += 13
            output.append(lch.lower_char(index))
        else:
            output.append(char)
    return ''.join(output)
