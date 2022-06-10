# https://leetcode.com/problems/add-digits/

class Solution(object):
    def addDigits(self, num):
        # If the number is a single digit return the number
        if num < 10:
            return num

        # Add up the digits in the number
        temp = 0
        for num in str(num):
            temp += int(num)

        # Run again with the new sum
        return self.addDigits(temp)
