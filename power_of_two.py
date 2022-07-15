# https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Handle edge case
        if n <= 0:
            return False
        return n & (n - 1) == 0
