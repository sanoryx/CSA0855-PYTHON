def concatenate_lists(list1, list2):
    for item in list1:
        yield item
    for item in list2:
        yield item

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(concatenate_lists(list1, list2))
print(result)
