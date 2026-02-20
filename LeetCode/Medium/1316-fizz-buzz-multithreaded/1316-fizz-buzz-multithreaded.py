from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.done = False  # tells worker threads to exit

        self.number_sem = Semaphore(1)
        self.fizz_sem = Semaphore(0)
        self.buzz_sem = Semaphore(0)
        self.fizzbuzz_sem = Semaphore(0)

    def fizz(self, printFizz):
        while True:
            self.fizz_sem.acquire()
            if self.done:
                return
            printFizz()
            self.i += 1
            self.number_sem.release()

    def buzz(self, printBuzz):
        while True:
            self.buzz_sem.acquire()
            if self.done:
                return
            printBuzz()
            self.i += 1
            self.number_sem.release()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            self.fizzbuzz_sem.acquire()
            if self.done:
                return
            printFizzBuzz()
            self.i += 1
            self.number_sem.release()

    def number(self, printNumber):
        while True:
            self.number_sem.acquire()

            if self.i > self.n:
                # mark done ONCE and unblock all workers so they can exit
                self.done = True
                self.fizz_sem.release()
                self.buzz_sem.release()
                self.fizzbuzz_sem.release()
                return

            if self.i % 15 == 0:
                self.fizzbuzz_sem.release()
            elif self.i % 3 == 0:
                self.fizz_sem.release()
            elif self.i % 5 == 0:
                self.buzz_sem.release()
            else:
                printNumber(self.i)
                self.i += 1
                self.number_sem.release()
