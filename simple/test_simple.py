import unittest

from simple.utils import generate_list_of_dicts, sort_list_of_dict


class TestSimple(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.list_case = [
            {'id': 1, 'edad': 16},
            {'id': 2, 'edad': 100},
            {'id': 3, 'edad': 90},
            {'id': 4, 'edad': 82},
            {'id': 5, 'edad': 59},
            {'id': 6, 'edad': 55},
            {'id': 7, 'edad': 39},
            {'id': 8, 'edad': 9},
            {'id': 9, 'edad': 90},
            {'id': 10, 'edad': 59}]

    def setUp(self):
        self.generated_list = generate_list_of_dicts()

    def test_generated_list(self):
        self.assertEqual(len(self.generated_list), 10)
        self.assertEqual(self.generated_list[0]['id'], 1)
        self.assertEqual(self.generated_list[-1]['id'], 10)
        self.assertEqual(type(self.generated_list[0]['edad']), int)

    def test_sorted_list(self):
        sorted_list = sort_list_of_dict(self.list_case)
        self.assertEqual(len(sorted_list), 10)
        self.assertEqual(sorted_list[0]['edad'], 100)
        self.assertEqual(sorted_list[-1]['edad'], 9)
        self.assertIn({'id': 6, 'edad': 55}, sorted_list)


if __name__ == '__main__':
    unittest.main()
