def get_avg_lists_intersection(lst1, lst2):
    intersection = set(lst1).intersection(lst2)
    numbers = []
    for el in lst1 + lst2:
        if el in intersection:
            numbers.append(el)
    if not numbers:
        return 0
    return round(sum(numbers) / len(numbers), 1)


def get_avg(lst1: list, lst2: list) -> float:
    inter = set(lst1) & set(lst2)
    numbers = [num for num in lst1 + lst2 if num in inter]
    return 0 if not numbers else round(sum(numbers) / len(numbers), 1)


if __name__ == '__main__':
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    print(get_avg_lists_intersection(lst1, lst2))
    print(get_avg(lst1, lst2))

# 1 1 1 2 2 4 5 7
# 1 2 2 3 5 6 6 8 12
