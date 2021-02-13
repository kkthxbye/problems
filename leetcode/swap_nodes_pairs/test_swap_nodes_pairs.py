from typing import List
from unittest import TestCase

from leetcode_swap_nodes_pairs import ListNode, swap_pairs


def create_head(seq: List[int]) -> ListNode:
    node = None
    for x in reversed(seq):
        node = ListNode(val=x, next=node)
    return node

def extract_nodes(head: ListNode) -> List[ListNode]:
    result = []
    node = head
    while node is not None:
        result.append(node)
        node = node.next
    return result


class Test(TestCase):

    def test_tree_even(self):
        """
        1, 2, 3, 4 -> 2, 1, 4, 3

        1 -> 2 -- 1 -> 4
        2 -> 3 -- 2 -> 1
        3 -> 4 -- 3 -> _
        4 -> _ -- 4 -> 3
        """
        head = create_head([1, 2, 3, 4])
        nodes = extract_nodes(head)
        self.assertEqual(
            [nodes[1], nodes[0], nodes[3], nodes[2]],
            extract_nodes(swap_pairs(head))
        )

    def test_tree_single(self):
        """
        1 -> _ -- 1 -> _
        """
        head = create_head([1])
        nodes = extract_nodes(head)
        self.assertEqual([nodes[0]], extract_nodes(swap_pairs(head)))

    def test_tree_odd(self):
        """
        1, 2, 3 -> 2, 1, 3

        1 -> 2 -- 1 -> 3
        2 -> 3 -- 2 -> 1
        3 -> _ -- 3 -> _
        """
        head = create_head([1, 2, 3])
        nodes = extract_nodes(head)
        self.assertEqual(
            [nodes[1], nodes[0], nodes[2]],
            extract_nodes(swap_pairs(head)),
        )
