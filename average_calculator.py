"""
Модуль для работы со списками чисел: вычисление среднего значения и их сравнение.
"""

class AverageCalculator:
    """
    Модуль для работы со списками чисел: вычисление среднего значения и их сравнение.
    """

    @staticmethod
    def calculate_average(numbers: list) -> float:
        """
        Рассчитывает среднее значение списка чисел.
        """
        if not numbers:
            raise ValueError("Список не должен быть пустым")
        return sum(numbers) / len(numbers)

    @staticmethod
    def compare_averages(list1: list, list2: list) -> str:
        """
        Сравнивает средние значения двух списков и возвращает результат.

        :param list1: Первый список чисел
        :param list2: Второй список чисел
        :return: Строка с результатом сравнения
        """
        avg1 = AverageCalculator.calculate_average(list1)
        avg2 = AverageCalculator.calculate_average(list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        if avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
