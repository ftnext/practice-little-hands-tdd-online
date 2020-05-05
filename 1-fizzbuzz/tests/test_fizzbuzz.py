from unittest import TestCase

from parameterized import parameterized

import fizzbuzz


class ExecuteTestCase(TestCase):
    @parameterized.expand([(1, "1"), (2, "2"), (4, "4")])
    def test_should_return_number_string(self, number, expected):
        actual = fizzbuzz.execute(number)
        self.assertEqual(actual, expected)

    def test_should_return_fizz(self):
        test_patterns = [
            (3, "Fizz"),
            (6, "Fizz"),
        ]
        for number, expected in test_patterns:
            with self.subTest(number=number, expected=expected):
                actual = fizzbuzz.execute(number)
                self.assertEqual(actual, expected)

    def test_should_return_buzz(self):
        test_patterns = [
            (5, "Buzz"),
            (10, "Buzz"),
        ]
        for number, expected in test_patterns:
            with self.subTest(number=number, expected=expected):
                actual = fizzbuzz.execute(number)
                self.assertEqual(actual, expected)

    def test_should_return_fizzbuzz(self):
        test_patterns = [
            (15, "FizzBuzz"),
            (30, "FizzBuzz"),
        ]
        for number, expected in test_patterns:
            with self.subTest(number=number, expected=expected):
                actual = fizzbuzz.execute(number)
                self.assertEqual(actual, expected)
