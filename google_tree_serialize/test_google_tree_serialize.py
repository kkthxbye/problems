from unittest import TestCase

from google_tree_serialize import Node, deserialize, serialize


class Test(TestCase):

    def test_foo(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        print(serialize(node))
        self.assertEqual('left.left', deserialize(serialize(node)).left.left.val)
