def get_avg(lst):
    """
    Принимает список чисел и возвращает среднее арифметическое
     чисел этого списка или 0, если список пуст
    >>> get_avg([1, 2, 3, 4, 5])
    3.0
    >>> get_avg([4, 4, 4])
    4.0
    >>> get_avg([])
    1
    """
    if not lst:
        return 0
    return sum(lst) / len(lst)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
