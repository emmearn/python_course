def diff_list(l1, l2=range(0, 5)):
    return [x for x in l1 if x not in l2]


print(diff_list(range(3, 8)))
