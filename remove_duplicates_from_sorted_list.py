# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution(object):
    def deleteDuplicates(self, head):
        curr_node = head

        while curr_node:
            if curr_node.next and curr_node.next.val == curr_node.val:
                # Skip over the dupplicate
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return head