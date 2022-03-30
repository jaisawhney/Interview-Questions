# Find the length of the longest substring without repeating characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# INPUT: string
# OUTPUT: int

# Example
# Input: s = "pwwkew"
# Output: 3

'''
Declare a dictionary to hold the characters
Loop through the characters in the string
Move the last position forward depending on the character's position
Update the result
Return result
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Declare a dictionary to hold the used characters
        used_chars = {}
        # Declare the result and previous position
        res, last_pos = 0, 0

        # Loop through the characters in the string
        for i, el in enumerate(s):
            # If the character has already been used move the last position to the used character's position
            # or stay the same. Whichever is bigger.
            if el in used_chars:
                last_pos = max(used_chars[el], last_pos)

            # Update the result
            res = max(res, i - last_pos + 1)

            # Change the index of the element to one more of where the character was last seen
            used_chars[el] = i + 1

        # Return result
        return res
