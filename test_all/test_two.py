import pytest

from files.code import get_avg


def test_mixed():
    assert get_avg([1, 2, 3, 4, 5]) == 3.0, 'Первая функция провалена'


def test_qual():
    assert get_avg([4, 4, 4]) == 4.0, "Второй тест провален"


def test_empty():
    assert get_avg([]) == 1, "Третий тест провален"


@pytest.mark.parametrize('lst, result', [([1, 2, 3, 4, 5], 3.0), ([4, 4, 4], 4.0), ([], 1)])
def test_sum(lst, result):
    assert get_avg(lst) == result, 'Что-то пошло не так'


@pytest.fixture
def dist_fix():
    return {1: {'value': [1, 2, 3, 4, 5],
                'result': 3.0},
            2: {'value': [4, 4, 4],
                'result': 4.0},
            3: {'value': [],
                'result': 1}
            }


def test_fixt(dist_fix):
    for key in dist_fix:
        item = dist_fix[key]
        assert get_avg(item['value']) == item['result'], 'Ошибка, брат'


if __name__ == '__main__':
    pytest.main()
