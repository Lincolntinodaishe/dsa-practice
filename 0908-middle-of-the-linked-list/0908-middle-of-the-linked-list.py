# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #pointers
        slow = head
        fast = head 
        # fast and fast.next should be valid always for us to get fast.nex.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow