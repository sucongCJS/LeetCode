class Node:
    def __init__(self, value):
        self.val = value
        self.pre = self.next = None

class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.curSize = 0
        # is it necessary to name head and tail seperately?
        # the answer is no： we only use the head.next and tail.pre, so they can be in the same add with diff name
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            # the order must be self.tail.pre.next = node, then self.tail.pre = node
            # according to the test so far, the assignment statement is executed from right to left
            self.tail.pre.next = self.tail.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.curSize > 0:
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
            self.curSize -= 1
            return True
        return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return self.head.next.val

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return self.tail.pre.val

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.curSize == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.curSize == self.size

if __name__ == "__main__":
    a = MyCircularQueue(8)
    print(a.enQueue(3))
    print(a.enQueue(9))
    print(a.enQueue(5))
    print(a.enQueue(0))
    print(a.deQueue())
    print(a.deQueue())
    print(a.isEmpty())
    print(a.isEmpty())
    print(a.Rear())
    print(a.Rear())
    print(a.deQueue())