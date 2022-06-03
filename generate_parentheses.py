# https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        def createParenthesis(res, curr, left, right):
            # No parenthesis left. Append the current set of parenthesis to the result
            if left == 0 and right == 0:
                res.append(curr)

            # Add an opening parenthesis to the result if valid
            if left > 0:
                createParenthesis(res, curr + '(', left - 1, right)

            # Add a closing parenthesis to the result if valid
            if right > left:
                createParenthesis(res, curr + ')', left, right - 1)
            return res

        return createParenthesis([], '', n, n)
