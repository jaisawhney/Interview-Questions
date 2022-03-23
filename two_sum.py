# Find the two numbers in a list that add up to the target
# https://leetcode.com/problems/two-sum/

# INPUT: list, target
# OUTPUT: list

# Example:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

'''
Create an empty dict
Loop through the numbers in the list
Get the difference between the target and the number
If the difference already exists in the dictionary return the value and index
Otherwise add the key and index to the dictionary
'''


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        # Loop over the numbers in the list
        for i, num in enumerate(nums):
            remaining = target - num
            # Check if the difference between the target and num is in the dict
            if remaining in seen:
                # Return the two numbers
                return [seen[remaining], i]
            # Add the num and index to the dict
            seen[num] = i
        # Return an empty list if no numbers add up
        return []


'''
Input: [3, 2, 4], target = 6

Loop 1:
remaining = 6 - 3 = 3
remaining not in seen
seen[3] = 0

Loop 2:
remaining = 6 - 2 = 4
remaining not in seen
seen[2] = 1

Loop 3:
remaining = 6 - 4 = 2
remaining in seen
return [seen[2], 2]
'''
