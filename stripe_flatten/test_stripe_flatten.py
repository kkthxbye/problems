from unittest import TestCase

from stripe_flatten import flatten_namespace


class TestStripeFlatter(TestCase):

    def test_flatten_namespace(self):
        self.assertEqual(
            {
                "key": 3,
                "foo.a": 5,
                "foo.bar.baz": 8
            },
            flatten_namespace({
                "key": 3,
                "foo": {
                    "a": 5,
                    "bar": {
                        "baz": 8
                    }
                }
            }
            )
        )
