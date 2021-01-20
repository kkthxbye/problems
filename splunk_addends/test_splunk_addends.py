from unittest import TestCase
from logging import basicConfig, DEBUG, getLogger
from sys import stderr

from splunk_addends import adds_up_to_n

basicConfig(stream=stderr, level=DEBUG)

logger = getLogger(__name__)


class Test(TestCase):

    def test_up_to_n(self):
        logger.debug('')
        self.assertEqual(
            frozenset(frozenset(x) for x in [
                [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-6, 1, 5],
            ]),
            adds_up_to_n([-8, -6, 1, 2, 3, 5, 6, 7, 12], target=0),
        )
