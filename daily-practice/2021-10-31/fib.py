class Solution:
    def __init__(self):
        self.cache = {}

    def fib(self, n):
        n_fib = self._fib(n)
        n_fibs = []
        for i in range(n):
            n_fibs.append(self.cache[i + 1])
        return n_fib, n_fibs

    def _fib(self, n):
        if n < -1:
            raise Exception("Invalid number!")
        elif n == 0:
            return 0
        elif n == 1:
            self.cache[n] = 1

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self._fib(n - 1) + self._fib(n - 2)
        return self.cache[n]


sol = Solution()
f = sol.fib(5)
print(f)
