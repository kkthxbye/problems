# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.index = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.index < len(self.nums) - 1

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if not self.hasNext():
            raise StopIteration
        self.index += 1
        return self.nums[self.index]

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        """
        self.iterator = iterator
        self.peeked = None


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        if self.peeked is None:
            self.peeked = self.next()
        return self.peeked


    def next(self):
        if self.peeked:
            peeked = self.peeked
            self.peeked = None
            return peeked
        return self.iterator.next()


    def hasNext(self):
        return self.peeked is not None or self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
iter = PeekingIterator(Iterator([1, 2, 3]))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    print(f'{val=}')
    actual = iter.next()         # Should return the same value as [val].
    print(f'{actual=}')
