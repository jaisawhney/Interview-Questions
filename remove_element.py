# Remove the occurrences of an element in a list
# https://leetcode.com/problems/remove-element/

# INPUT: list, item
# OUTPUT: # of remaining items

# Example:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

'''
Declare a counter with the value of 0
Iterate through the numbers in the inputted list
If the number does not equal the target shift the items in the list
Return the count of unremoved items
'''


class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        # Loop through the list
        for i in range(len(nums)):
            # Check if the number is the target
            if nums[i] != val:
                # Shift items over
                nums[count] = nums[i]
                count += 1
        # Return the count
        return count
