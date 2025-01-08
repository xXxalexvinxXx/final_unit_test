import pytest
from average_calculator import AverageCalculator


class TestAverageCalculator:
    def test_calculate_average_positive(self):
        assert AverageCalculator.calculate_average([1, 2, 3, 4, 5]) == 3.0

    def test_calculate_average_negative(self):
        assert AverageCalculator.calculate_average([-5, -10, -15]) == -10.0

    def test_calculate_average_mixed(self):
        assert AverageCalculator.calculate_average([-2, 3, -4, 5]) == 0.5

    def test_calculate_average_empty(self):
        with pytest.raises(ValueError):
            AverageCalculator.calculate_average([])

    def test_compare_averages_first_larger(self):
        result = AverageCalculator.compare_averages([5, 10], [2, 3])
        assert result == "Первый список имеет большее среднее значение"

    def test_compare_averages_second_larger(self):
        result = AverageCalculator.compare_averages([1, 2], [10, 20])
        assert result == "Второй список имеет большее среднее значение"

    def test_compare_averages_equal(self):
        result = AverageCalculator.compare_averages([5, 5], [5, 5])
        assert result == "Средние значения равны"
