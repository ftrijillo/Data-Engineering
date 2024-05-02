def remove_duplicates(input_list):
    if len(input_list) >= 0:
        res = [i for n, i in enumerate(input_list) if i not in input_list[:n]]
        return res


print(remove_duplicates([1, 2, 3, "apple", "banana", 3]))
