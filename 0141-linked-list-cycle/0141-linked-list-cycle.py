# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
                # use fast and slow pointers
        fast = head
        slow = head
        # check if fast and fast.next are still valid because if fast is none that means wve
        # reached the ends of our list and fast.next becomes an attrbute error
        # but if both are still valid we can safely get to fast.next.next
        while fast and fast.next:
            # move fast two steps
            # slow one step
            fast = fast.next.next
            slow = slow.next
            # if at any point we find slow == fast then we have a cycle detected
            # return true
            if slow == fast:
                return True
        return False