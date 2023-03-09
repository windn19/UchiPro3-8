import unittest

from files.code import get_avg


class TestGetAvg(unittest.TestCase):
    """Тестируем get_avg."""
    def setUp(self) -> None:
        print('Начальные установки')

    def test_mixed_numbers(self):
        result = get_avg([1, 2, 3, 4, 5])
        expected = 3.0
        self.assertEqual(result, expected, 'Функция должна возвращать среднее арифметическое')

    def test_equal_numbers(self):
        result = get_avg([4, 4, 4])
        expected = 4.0
        self.assertEqual(result, expected, 'Функция должна возвращать среднее арифметическое')

    def test_empty(self):
        result = get_avg([])
        expected = 1
        self.assertEqual(result, expected, 'Функция должна возвращать 0 для пустого списка')

    def tearDown(self) -> None:
        print('Завершение работы')


if __name__ == '__main__':
    unittest.main()