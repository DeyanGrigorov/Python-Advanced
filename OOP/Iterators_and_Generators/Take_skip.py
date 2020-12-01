class take_skip:
    def __init__(self, step, count=0):
        self.count = count
        self.step = step
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        val = self.current
        self.current += self.step
        generated_till_now = (val / self.step)
        if generated_till_now == self.count:
            raise StopIteration
        return val


