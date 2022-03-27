# Convert a roman numeral to an integer
# https://leetcode.com/problems/roman-to-integer/

# INPUT: string
# OUTPUT: int

# Example:
# Input: s = "LVIII"
# Output: 58

'''
Declare a dictionary with the roman numerals and their integer equivalents
Loop through the length of the string, skipping the last numeral
If the current numeral is less than the next numeral subtract from the total, otherwise add to the total
Add the int value of the last numeral to the total and return the total
'''


class Solution(object):
    def romanToInt(self, s):
        # Dictionary of the roman numeral equivalents
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Declare a variable to count the int values
        num = 0

        # Loop through the length of the string minus one (skip the last numeral)
        for i in range(len(s) - 1):
            # If the current numeral is less than the next numeral subtract
            if roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                num -= roman_numerals[s[i]]

            # Otherwise add
            else:
                num += roman_numerals[s[i]]

        # Return the number plus the value of the last numeral
        return num + roman_numerals[s[-1]]
