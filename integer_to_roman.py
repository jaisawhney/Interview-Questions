# https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        # Dictionary to translate integers to their numeral counterpart
        numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        roman_numeral = ''

        # Loop through the numerals
        for integer in numerals:
            # While the target number is greater than zero
            while num > 0:
                # Break the loop if the integer in the dict is larger than the target
                if integer > num:
                    break

                # Add the numeral to the result
                roman_numeral += numerals[integer]

                # Subtract the integer from the target
                num -= integer

        return roman_numeral

