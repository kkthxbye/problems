from unittest import TestCase

from fizzbuzz import fizzbuzz


class Test(TestCase):

    def test_foo(self):
        self.assertEqual([
            '1', '2',
            'Fizz',
            '4',
            'Buzz', 'Fizz',
            '7', '8',
            'Fizz', 'Buzz',
            '11',
            'Fizz',
            '13', '14',
            'FizzBuzz',
        ], list(fizzbuzz(range(1, 16))))
