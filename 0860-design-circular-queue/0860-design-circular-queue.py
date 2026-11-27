class MyCircularQueue:

    def __init__(self, k: int):
        self.a = [0] * k
        self.size = 0
        self.n = k
        self.f = 0
        self.r = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.r = (self.r + 1) % self.n
        self.a[self.r] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.a[self.f] = 0
        self.f = (self.f + 1) % self.n
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.a[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.a[self.r]

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.n:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()