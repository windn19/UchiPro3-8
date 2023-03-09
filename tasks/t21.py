def get_avg_unique_lists(lst1: list, lst2: list) -> float:
    """
    >>> get_avg_unique_lists([1, 2], [3])
    2.0
    >>> get_avg_unique_lists([], [])
    0
    """
    unique = []
    for lst in lst1, lst2:
        d = {}
        for num in lst:
            d[num] = d.get(num, 0) + 1
        # print(d)
        unique.extend([key for key, val in d.items() if val == 1])
        # print(unique)
    if not unique:
        return 0
    return round(sum(unique) / len(unique), 1)


# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# print(get_avg_unique_lists(lst1, lst2))

# 1 1 1 2 3 3 4 5 5
# 1 1 2 3 5 6 7 7