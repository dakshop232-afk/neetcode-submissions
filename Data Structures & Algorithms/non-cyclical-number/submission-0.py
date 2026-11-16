class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum_val = 0
            while n > 0:
                rem = n % 10
                sum_val = sum_val + (rem**2)
                n = n // 10
            n = sum_val

        return n == 1