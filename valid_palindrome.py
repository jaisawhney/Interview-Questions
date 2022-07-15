# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        string_list = [char.lower() for char in s if char.isalnum()]
        left, right = 0, len(string_list) - 1
        while left < right:
            if string_list[left] != string_list[right]:
                return False
            left = left + 1
            right = right - 1
        return True
