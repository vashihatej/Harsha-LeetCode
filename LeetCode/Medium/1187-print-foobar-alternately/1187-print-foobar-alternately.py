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
