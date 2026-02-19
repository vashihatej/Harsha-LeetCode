from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        
        # Start with foo allowed to run
        self.foo_sem = Semaphore(1)
        
        # bar must wait initially
        self.bar_sem = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            
            # Wait until it's foo's turn
            self.foo_sem.acquire()
            
            # Print "foo"
            printFoo()
            
            # Allow bar to run
            self.bar_sem.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            
            # Wait until foo has printed
            self.bar_sem.acquire()
            
            # Print "bar"
            printBar()
            
            # Allow foo to run next
            self.foo_sem.release()


# from threading import Condition

# class FooBar:
#     def __init__(self, n):
#         self.n = n
        
#         # Condition object internally contains a lock
#         self.cond = Condition()
        
#         # Shared state variable to control whose turn it is
#         # 0 -> foo's turn
#         # 1 -> bar's turn
#         self.turn = 0

#     def foo(self, printFoo: 'Callable[[], None]') -> None:
#         for _ in range(self.n):
#             with self.cond:
                
#                 # Wait until it is foo's turn
#                 while self.turn != 0:
#                     self.cond.wait()
                
#                 # Now safe to print
#                 printFoo()
                
#                 # Change turn to bar
#                 self.turn = 1
                
#                 # Wake up waiting threads (bar thread)
#                 self.cond.notify()

#     def bar(self, printBar: 'Callable[[], None]') -> None:
#         for _ in range(self.n):
#             with self.cond:
                
#                 # Wait until it is bar's turn
#                 while self.turn != 1:
#                     self.cond.wait()
                
#                 # Now safe to print
#                 printBar()
                
#                 # Change turn back to foo
#                 self.turn = 0
                
#                 # Wake up foo thread
#                 self.cond.notify()

