import threading


class DiningPhilosophers:

    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(
        self,
        philosopher,
        pickLeftFork,
        pickRightFork,
        eat,
        putLeftFork,
        putRightFork
    ):
        # LeetCode fork mapping:
        # left fork = (philosopher + 1) % 5
        # right fork = philosopher
        left = (philosopher + 1) % 5
        right = philosopher

        # Acquire forks in different orders to prevent deadlock.
        if philosopher % 2 == 0:
            first, second = left, right
        else:
            first, second = right, left

        self.forks[first].acquire()
        self.forks[second].acquire()

        try:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
        finally:
            self.forks[second].release()
            self.forks[first].release()
