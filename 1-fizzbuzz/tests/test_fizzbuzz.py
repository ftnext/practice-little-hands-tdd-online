from unittest import TestCase

import fizzbuzz


class CreateTestCase(TestCase):
    def test_should_return_number_string(self):
        test_patterns = [
            (1, "1"),
            (2, "2"),
            (4, "4"),
        ]
        for number, expected in test_patterns:
            with self.subTest(number=number, expected=expected):
                actual = fizzbuzz.create(number)
                self.assertEqual(actual, expected)

    def test_fizzbuzz_3(self):
        actual = fizzbuzz.create(3)
        self.assertEqual(actual, "Fizz")

    def test_should_return_buzz(self):
        actual = fizzbuzz.create(5)
        self.assertEqual(actual, "Buzz")
