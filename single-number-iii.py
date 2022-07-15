# https://leetcode.com/problems/single-number/submissions/

class Solution(object):
    def singleNumber(self, nums):
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        res = []
        for el in seen:
            if seen[el] == 1:
                res.append(el)
        return res
