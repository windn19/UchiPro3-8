def get_avg(lst):
    if not lst:
        return 0
    # print(sum(lst))
    # print(len(lst))
    return sum(lst) / len(lst)


for lst in [[1, 2, 3, 4, 5], [4, 4, 4], [], [0, 0, 0]]:
    print(f'{str(lst):<20} -> {get_avg(lst):^8}')