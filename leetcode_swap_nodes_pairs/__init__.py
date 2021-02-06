from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: 'ListNode'


def swap_pairs(head: ListNode) -> ListNode:
    node = head
    new_head = None
    while node is not None:
        paired_node = node.next
        if new_head is None:
            new_head = paired_node if paired_node is not None else node
        if paired_node is not None:
            next_pair = paired_node.next
            node.next = (next_pair.next
                         if next_pair is not None and next_pair.next is not None
                         else next_pair)
            paired_node.next = node

            node = next_pair
        else:
            node = None
    return new_head
