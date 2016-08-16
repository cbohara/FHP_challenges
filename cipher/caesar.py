import cipher_helper as ch

def rot13(input_string):
    """Rotates each letter in the string by 13 characters, maintaining capitalization and spaces."""
    string = list(input_string)
    output = []
    for char in string:
        if char.isupper():
            index = ch.upper_index(char)
            index += 13
            output.append(ch.upper_char(index))
        elif char.islower():
            index = ch.lower_index(char)
            index += 13
            output.append(ch.lower_char(index))
        else:
            output.append(char)
    return ''.join(output)
