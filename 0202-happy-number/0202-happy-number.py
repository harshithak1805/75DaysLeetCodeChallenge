class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(x: int) -> int:
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)
        return n == 1