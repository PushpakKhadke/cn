def encoded_string(input_string):
    encoded = ""
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded += f"{current_char}({count}) "
            current_char = char
            count = 1
    encoded += f"{current_char}({count}) "
    return encoded

input_string = input("Enter String = ")
print("Output String  = ",encoded_string(input_string))