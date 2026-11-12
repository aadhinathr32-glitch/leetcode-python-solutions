class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.deque = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.size
        self.deque[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1) % self.size
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        index = (self.rear - 1) % self.size
        return self.deque[index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Sample test
myCircularDeque = MyCircularDeque(3)
assert myCircularDeque.insertLast(1) is True
assert myCircularDeque.insertLast(2) is True
assert myCircularDeque.insertFront(3) is True
assert myCircularDeque.insertFront(4) is False
assert myCircularDeque.getRear() == 2
assert myCircularDeque.isFull() is True
assert myCircularDeque.deleteLast() is True
assert myCircularDeque.insertFront(4) is True
assert myCircularDeque.getFront() == 4

print("All sample tests passed.")
