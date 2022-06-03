# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution(object):
    def searchRange(self, nums, target):
        # Binary search for the first index
        def find_first_idx(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (right + left) // 2

                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        # Binary search for the last index
        def find_last_idx(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (right + left) // 2

                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        # Return the first and last positions if valid
        first_idx, last_idx = find_first_idx(nums, target), find_last_idx(nums, target)
        if first_idx <= last_idx:
            return [first_idx, last_idx]
        else:
            return [-1, -1]
