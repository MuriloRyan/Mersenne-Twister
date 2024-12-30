class MersenneTwister:
    def __init__(self, seed: int = 0, w: int = 32):
        self.state = [0] * 624
        self.state[0] = seed

        self.a = 0x9908B0DF
        self.b = 0x9d2c5680
        self.c = 0xEFC60000
        self.u = 11
        self.d = 0xFFFFFFFF
        self.s = 7
        self.t = 15
        self.l = 18
        self.f = 1812433253
        self.r = 31
        self.w = w

        self.upper_mask = (1 << (self.w - self.r))
        self.lower_mask = (1 << self.r) - 1

        self._start()
        
        self.index = 1

    def _start(self):
        for i in range(623):
            self.state[i+1] = self.f * (self.state[i-1] ^(self.state[i - 1]) >> (self.w - 2)) + i % (2**self.w)

        return self.state
    
    def _generate_numbers(self):
        for i in range(624):
            y = (self.state[i] & self.upper_mask) + (self.state[i + 1] & self.lower_mask)
            self.state[i] = self.state[i + self.m] ^ (y >> 1)

        return self.state
    
    def get(self):
        if self.index > 624:
            self.index = 1
            return self.get()
        
        self.index += 1

        z = self.state[self.index]

        z = z ^ ((z >> self.u) & self.d)
        z = z ^ ((z << self.s) & self.b)
        z = z ^ ((z << self.t) & self.c)
        z = z ^ (z >> self.l)

        return z  

seed = 123

mt = MersenneTwister(seed=seed)
index = 1

from time import sleep
while True:
    print(f"index ({index}) = " + str(mt.get().bit_length())) 
    sleep(1)
    index += 1