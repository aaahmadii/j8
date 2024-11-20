def invert_dictionary(input_dict):
    inverted_dict = {value: key for key, value in input_dict.items()}
    return inverted_dict

input_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

result = invert_dictionary(input_dict)
print(result)  
