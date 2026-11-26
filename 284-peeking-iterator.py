class PeekingIterator:

    def __init__(self, iterator):
        self.iterator = iterator
        self.next_value = None

        if iterator.hasNext():
            self.next_value = iterator.next()

    def peek(self):
        return self.next_value

    def next(self):
        value = self.next_value

        if self.iterator.hasNext():
            self.next_value = self.iterator.next()
        else:
            self.next_value = None

        return value

    def hasNext(self):
        return self.next_value is not None
