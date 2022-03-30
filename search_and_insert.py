# Return the index of the target or where it would be inserted in order
# https://leetcode.com/problems/search-insert-position/

# INPUT: list (sorted)
# OUTPUT: int

# Example
# Input: nums = [1,3,5,6], target = 7
# Output: 4

'''
Declare left and right variables
Loop while left is less than or equal to right
If the target is lower than the middle remove the bigger elements
Otherwise remove the smaller elements
Return the result
'''

# SOLUTION 1 - Binary search
class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            # Calculate the middle of the list
            mid = (right + left) // 2

            # Check if the target is lower than the middle
            if target <= nums[mid]:
                # Remove the bigger elements
                right = mid - 1

            # Otherwise
            else:
                # Remove the smaller elements
                left = mid + 1

        # Return the index
        return left
