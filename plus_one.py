# https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        str_digits = ''.join([str(digit) for digit in digits])
        num_digits = int(str_digits)

        list_digits = [int(digit) for digit in str(num_digits + 1)]
        return list_digits
