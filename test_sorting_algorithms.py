import unittest
import time
from sorting_algorithms import bubble_sort, selection_sort, quick_sort  # Import the sorting functions
import random

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.test_data = [random.randint(1, 1000) for _ in range(1000)]

    def test_bubble_sort(self):
        start_time = time.time()
        sorted_data = bubble_sort(self.test_data.copy())
        end_time = time.time()
        self.assertEqual(sorted_data, sorted(self.test_data))
        print(f"Время пузырьковой сортировки: {end_time - start_time:.3f} ms")

    def test_selection_sort(self):
        start_time = time.time()
        sorted_data = selection_sort(self.test_data.copy())
        end_time = time.time()
        self.assertEqual(sorted_data, sorted(self.test_data))
        print(f"Время выборочной сортировки: {end_time - start_time:.3f} ms")

    def test_quick_sort(self):
        start_time = time.time()
        sorted_data = quick_sort(self.test_data.copy())
        end_time = time.time()
        self.assertEqual(sorted_data, sorted(self.test_data))
        print(f"Время быстрой сортировки: {end_time - start_time:.3f} ms")

if __name__ == '__main__':
    unittest.main()
