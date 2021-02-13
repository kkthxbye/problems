from dataclasses import dataclass
from typing import List
from itertools import chain


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None


def toListNode(vals: List[int]) -> ListNode:
    head = ListNode()
    prev = None
    for value in reversed(vals):
        if prev is not None:
            head = ListNode(value)
            head.next = prev
        else:
            head.val = value
        prev = head
    return head


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    current = head
    carry = 0
    while l1 or l2 or carry:
        carry, value = divmod(sum(chain((x.val if x else 0 for x in [l1, l2]), [carry])), 10)
        current.next = ListNode(val=value)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head.next


# print(toListNode([2, 4, 3]))


# print(addTwoNumbers(toListNode([2, 4, 3]), toListNode([5, 6, 4])))

# print(addTwoNumbers(toListNode([2, 4]), toListNode([5, 6, 4])))

print(addTwoNumbers(*[toListNode(x) for x in [
    [9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9],
]]))
