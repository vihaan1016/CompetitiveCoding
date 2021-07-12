class PriorityQueue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self, value):
        self.queue.append(value)
    def delete(self):
        max = 0
        try:
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(1)
    myQueue.insert(2)
    myQueue.insert(3)
    myQueue.insert(4)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())