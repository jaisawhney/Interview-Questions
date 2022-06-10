# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        # Dictionary to map digits to the available letters
        mapping = {
            "0": " ",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        # Loop through each digit in the input
        for num in digits:
            # Keep track of the current digit's combo
            running_combo = []

            # Loop through each possible letter for the digit
            for letter in mapping[num]:

                # Loop through the already existing combos (if exists) and add the next possible letter
                for com in res or ['']:
                    running_combo.append(com + letter)

            # Set the result to the current digit's combo
            res = running_combo
        return res
