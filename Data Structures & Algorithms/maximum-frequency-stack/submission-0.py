class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        
        f = self.freq[val] 

        if f > self.max_freq:
            self.max_freq = f
        
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)
        

    def pop(self) -> int:
        vals_at_max = self.group[self.max_freq]
        vals = vals_at_max.pop()

        self.freq[vals] -= 1

        if len(vals_at_max) == 0:
            self.max_freq -= 1

        return vals        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()