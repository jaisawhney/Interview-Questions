# https://leetcode.com/problems/contains-duplicate/

# Attempt one - too slow
class Solution(object):
    def containsDuplicate(self, nums):
        seen = []

        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False

# Attempt two

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            seen.add(num)
        return len(seen) != len(nums)