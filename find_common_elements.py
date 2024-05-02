def find_common_elements(list1, list2):
    if len(list1) >= 0 and len(list2) >= 0:
        set1 = set(list1)
        set2 = set(list2)

        return list(set1.intersection(set2))
    else:
        return []


print(find_common_elements([1, 2, 4], [1, 2, 3]))
