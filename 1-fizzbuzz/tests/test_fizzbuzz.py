from unittest import TestCase

import fizzbuzz


class CreateTestCase(TestCase):
    def test_fizzbuzz_1(self):
        actual = fizzbuzz.create(1)
        self.assertEqual(actual, "1")

    def test_fizzbuzz_2(self):
        actual = fizzbuzz.create(2)
        self.assertEqual(actual, "2")

    def test_fizzbuzz_3(self):
        actual = fizzbuzz.create(3)
        self.assertEqual(actual, "Fizz")
