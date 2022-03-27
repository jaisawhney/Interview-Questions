# Finding the majority element (element that appears more than length/2 )
# https://leetcode.com/problems/majority-element/

# INPUT: list
# OUTPUT: int

# Example:
# Input: nums = [3,2,3]
# Output: 3

'''
Declare what the majority count is
Loop through the numbers in the list
If the total occurrences of the element is more than the majority count return the number
'''


class Solution:
    def majorityElement(self, nums):
        # Declare what the majority count is
        majority_count = len(nums) // 2

        # Loop through the numbers
        for num in nums:
            # Count up the number of occurrences for an element
            count = sum(1 for elem in nums if elem == num)

            # Check if the count is more than the majority
            if count > majority_count:
                # Return the number
                return num
