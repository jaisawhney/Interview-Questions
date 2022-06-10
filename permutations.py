# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        res = []

        # If the length of the list is 1 return the list
        if (len(nums) == 1):
            return [nums]

        # Loop through the possible digits
        for i in range(len(nums)):
            # Permute throughout the remaining digits
            permutations = self.permute(nums[:i] + nums[i + 1:])

            # Append the removed value back to the permutations
            for permutation in permutations:
                permutation.append(nums[i])

            # Append to the result
            res.extend(permutations)
        return res
