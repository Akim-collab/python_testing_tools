from one_hot_encoder import fit_transform
import unittest


class TestOneHotEncoder(unittest.TestCase):
    def first_base_test(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(exp_transformed_cities, fit_transform(cities))

    def test_one_word(self):
        cities = ['Moscow', 'Moscow', 'Moscow', 'Moscow']
        exp_transformed_cities = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        self.assertEqual(exp_transformed_cities, fit_transform(cities))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_single_argument(self):
        input_data = "abcde"
        expected_output = [
            ("a", [0, 0, 0, 0, 0]),
            ("b", [1, 0, 0, 0, 0]),
            ("c", [0, 1, 0, 0, 0]),
            ("d", [1, 1, 0, 0, 0]),
            ("e", [0, 0, 1, 0, 0])
        ]
        self.assertEqual(fit_transform(input_data), expected_output)

    def test_non_string_argument(self):
        input_data = [1, 2, 3]
        expected_output = [
            (1, [0, 0, 1]),
            (2, [1, 0, 0]),
            (3, [0, 1, 0])
        ]
        self.assertEqual(fit_transform(input_data), expected_output)


if __name__ == '__main__':
    unittest.main()
