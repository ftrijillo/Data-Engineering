def merge_sorted_lists(list1, list2):

    if len(list1) == 0 and len(list2) == 0:
        return []

    elif len(list1) == 0:
        list2.sort()
        return list2

    elif len(list2) == 0:
        list1.sort()
        return list1

    new_list = list1
    new_list.extend(list2)

    new_list.sort()
    return new_list


print(merge_sorted_lists([], []))
