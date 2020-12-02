class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.current_index = 0

    def __next__(self):
        if self.counter < self.number:
            if self.current_index == len(self.sequence):
                self.current_index = 0
            self.current_index += 1
            self.counter += 1
            return self.sequence[self.current_index - 1]
        raise StopIteration

    def __iter__(self):
        return self


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')