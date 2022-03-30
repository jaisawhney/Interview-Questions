# Given a list with heights, calculate a container that can contain the most water
# https://leetcode.com/problems/container-with-most-water/

# INPUT: list
# OUTPUT: int

# Example
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

'''
Declare a variable to hold the area
Loop through each height and each height plus one to consider every possible solution
For each iteration set the result to the calculated area if the area is greater than the existing result
Return result
'''


class Solution(object):
    def maxArea(self, height):
        # Declare a variable to hold the area
        res = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                # Width
                w = j - i

                # Height
                h = min(height[i], height[j])

                # Area
                area = w * h

                # Set the result to either the area only if the area is greater than the current result
                res = max(area, res)

        # Return the result
        return res
