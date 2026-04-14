# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #floyd cylcle detection algorithm
        #if fast and slow pointer meets, the distance of slow to the
        #strt of the cylcle == the distance of the head to the start of the cycle
        tracker = head
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while slow != tracker:
                    slow = slow.next
                    tracker = tracker.next
                return slow
        return None
                
        