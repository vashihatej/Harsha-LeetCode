from threading import Lock

class DiningPhilosophers:

    def __init__(self):
        # Create 5 locks representing 5 forks
        # Only one philosopher can hold a fork at a time
        self.forks = [Lock() for _ in range(5)]

    def wantsToEat(self, philosopher: int,
                   pickLeftFork,
                   pickRightFork,
                   eat,
                   putLeftFork,
                   putRightFork):

        # Fork indices
        left = philosopher
        right = (philosopher + 1) % 5

        # 🔥 Deadlock Prevention Strategy:
        # Always pick lower-numbered fork first
        first = min(left, right)
        second = max(left, right)

        # Acquire forks in global order
        self.forks[first].acquire()
        self.forks[second].acquire()

        # Now we own both forks.
        # But we must call pickLeftFork and pickRightFork
        pickLeftFork()
        pickRightFork()

        # Eat
        eat()

        # Put forks down in reverse logical order
        putLeftFork()
        putRightFork()

        # Release locks
        self.forks[second].release()
        self.forks[first].release()


# from threading import Semaphore, Lock

# class DiningPhilosophers:

#     def __init__(self):
#         # Each fork is a lock (only one philosopher can hold it)
#         self.forks = [Lock() for _ in range(5)]

#         # Allow at most 4 philosophers to try picking forks
#         # This prevents circular deadlock
#         self.table = Semaphore(4)

#     def wantsToEat(self, philosopher,
#                    pickLeftFork,
#                    pickRightFork,
#                    eat,
#                    putLeftFork,
#                    putRightFork):

#         left = philosopher
#         right = (philosopher + 1) % 5

#         # Limit entry to 4 philosophers at a time
#         self.table.acquire()

#         # Pick forks (locks guarantee mutual exclusion)
#         self.forks[left].acquire()
#         pickLeftFork()

#         self.forks[right].acquire()
#         pickRightFork()

#         # Eat
#         eat()

#         # Put forks down
#         putRightFork()
#         self.forks[right].release()

#         putLeftFork()
#         self.forks[left].release()

#         # Leave table
#         self.table.release()

