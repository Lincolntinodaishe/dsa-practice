# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty return None value
        if not head or not head.next:
            return None
        # fast and slow pointer to locate the middle node
        # prev pointer that keep count of the node before the middle node
        fast = slow = head
        prev = None

        while fast and fast.next:
            prev = slow #prev will be eqal to slow b4 we update slow so as to keep trak of the node before the middle
            fast= fast.next.next
            slow = slow.next
        
        #prev.next = slow.next
        prev.next = prev.next.next

        return head