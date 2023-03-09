def get_avg_unique(lst):
    numbers = dict()
    for num in lst:
        if num not in numbers:
            numbers[num] = 1
        else:
            numbers[num] += 1
    # print(numbers)
    unique = [key for key in numbers if numbers[key] == 1]
    if not unique:
        return 0
    return round(sum(unique) / len(unique), 1)


# lst = list(map(int, input().split()))
# print(get_avg_unique(lst))
assert get_avg_unique([1, 1, 2, 2]) == 0
assert get_avg_unique([2, 2, 3, 4, 4, 5]) == 4.0
assert get_avg_unique([]) == 0

lst = list(map(int, input().split()))
print(get_avg_unique(lst))

# 1 1 1 2 3 3 4 5 5