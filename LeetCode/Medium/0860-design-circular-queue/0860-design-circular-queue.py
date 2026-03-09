class MyCircularQueue:

    def __init__(self, k):
        self.data = [0] * k    # fixed-size array
        self.size = k          # max capacity
        self.front = 0         # index of the front element
        self.count = 0         # how many elements currently stored

    def enQueue(self, value):
        # Can't add if full
        if self.isFull():
            return False

        # Where does the new element go?
        # It goes right AFTER the current last element.
        # Current last element is at (front + count - 1) % size
        # So next open slot is at (front + count) % size
        insert_at = (self.front + self.count) % self.size
        self.data[insert_at] = value
        self.count += 1
        return True

    def deQueue(self):
        # Can't remove if empty
        if self.isEmpty():
            return False

        # "Remove" the front element by moving front forward
        # No need to actually clear the value — it'll be overwritten later
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        # Last element is at (front + count - 1) % size
        rear_idx = (self.front + self.count - 1) % self.size
        return self.data[rear_idx]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
