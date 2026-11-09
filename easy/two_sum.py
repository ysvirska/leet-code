"""1. Two Sum — Easy.
https://leetcode.com/problems/two-sum/

Даны список целых чисел nums и целое число target. Вернуть индексы двух
разных элементов, сумма которых равна target. Гарантируется ровно одна
подходящая пара. Порядок индексов в ответе не важен.

Примеры:
    nums = [2, 7, 11, 15], target = 9 -> [0, 1]
    nums = [3, 2, 4], target = 6 -> [1, 2]
    nums = [3, 3], target = 6 -> [0, 1]

Ограничения:
    2 <= len(nums) <= 10**4
    -10**9 <= nums[i], target <= 10**9
    Существует ровно одно решение.

Алгоритм: храним в словаре индексы уже просмотренных чисел. Для каждого
числа ищем дополнение target - число. Проверяем словарь до добавления
текущего числа, чтобы не использовать один элемент дважды.

Сложность: O(n) времени в среднем, O(n) дополнительной памяти.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index

        raise ValueError("Входные данные должны содержать подходящую пару")
