from threading import Event

class Foo:
    def __init__(self):
        # Event is a synchronization primitive.
        # It acts like a boolean flag that starts as False.
        # 
        # .wait()  -> blocks until the event is set
        # .set()   -> sets the flag to True and wakes all waiting threads
        #
        # We use two events:
        # 1. first_done  -> signals that first() finished
        # 2. second_done -> signals that second() finished

        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # This method can run immediately (no dependency).

        # printFirst() outputs "first".
        printFirst()

        # Signal that first() has completed.
        # Any thread waiting on first_done.wait() will now proceed.
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # second() must wait until first() completes.
        # If first_done is not set, this blocks.
        self.first_done.wait()

        # Now it is safe to print "second".
        printSecond()

        # Signal that second() has completed.
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # third() must wait until second() completes.
        self.second_done.wait()

        # Now safe to print "third".
        printThird()


# from threading import Condition

# class Foo:
#     def __init__(self):
#         # Condition combines:
#         # 1. A lock (for mutual exclusion)
#         # 2. A waiting mechanism (wait/notify)
#         #
#         # We use a shared state variable to track execution order.
#         self.cond = Condition()
#         self.state = 1   # 1 = first allowed, 2 = second allowed, 3 = third allowed

#     def first(self, printFirst):
#         with self.cond:
#             printFirst()
#             self.state = 2        # Allow second()
#             self.cond.notify_all()  # Wake up waiting threads

#     def second(self, printSecond):
#         with self.cond:
#             # Always use while, not if.
#             # This protects against spurious wakeups.
#             while self.state != 2:
#                 self.cond.wait()
#             printSecond()
#             self.state = 3
#             self.cond.notify_all()

#     def third(self, printThird):
#         with self.cond:
#             while self.state != 3:
#                 self.cond.wait()
#             printThird()


# from threading import Semaphore

# class Foo:
#     def __init__(self):
#         # Semaphore(0) means:
#         # acquire() will block until release() is called.
#         #
#         # sem1 controls second()
#         # sem2 controls third()
#         self.sem1 = Semaphore(0)
#         self.sem2 = Semaphore(0)

#     def first(self, printFirst):
#         printFirst()
#         # Allow second() to proceed
#         self.sem1.release()

#     def second(self, printSecond):
#         # Wait until first() releases sem1
#         self.sem1.acquire()
#         printSecond()
#         # Allow third() to proceed
#         self.sem2.release()

#     def third(self, printThird):
#         # Wait until second() releases sem2
#         self.sem2.acquire()
#         printThird()
