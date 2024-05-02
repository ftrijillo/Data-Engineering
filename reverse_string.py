def reverse_string(input_string):
    input_list = list(input_string)
    input_list.reverse()
    return "".join(input_list)


print(reverse_string("Python is great"))
