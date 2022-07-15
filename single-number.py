# https://leetcode.com/problems/single-number/submissions/

class Solution(object):
    def singleNumber(self, nums):
        seen_elements = {}
        for num in nums:
            seen_elements[num] = seen_elements.get(num, 0) + 1

        return min(seen_elements, key=seen_elements.get)
