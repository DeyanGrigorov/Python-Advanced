class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = 0

    def __iter__(self):
        self.end = 0
        return self

    def __next__(self):
        val = self.count
        if self.end == self.count + 1:
            raise StopIteration
        self.count -= 1
        return val


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")





