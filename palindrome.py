# Check if an integer is a palindrome or not
# https://leetcode.com/problems/palindrome-number/


# SOLUTION 1 - String solution

# INPUT: int
# OUTPUT: bool


'''
Convert int to a string
Reverse string and compare if they are equal
'''


class Solution:
    def isPalindrome(self, x):
        # Convert the digits to a string
        str_numbers = str(x)

        # Reverse the string
        rev_string = str_numbers[::-1]

        # Checks if the reverse is equal to the original
        return rev_string == str_numbers


# SOLUTION 2 - No strings

# INPUT: int
# OUTPUT: bool

'''
Declare an integer to store the reverse
Add the numbers in reverse to the variable
Compare the reversed number to the original and return the result
'''


class Solution:
    def isPalindrome(self, x):
        orig_num = x
        rev_num = 0
        # Add the numbers in reverse
        while x > 0:
            # Get the last digit
            last_digit = x % 10

            # Remove the last digit
            x = x // 10

            # Add the last digit to the list
            rev_num = rev_num * 10 + last_digit

        # Checks if the reverse is equal to the original
        return orig_num == rev_num
