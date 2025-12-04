# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     
        dummy = ListNode()
        dummy.next = head
        #create a dummy for edge cases where you have to remove the head
        ahead = before = dummy
        # us e two pointers one that goes ahead and that stays behind

        '''
        Logic : move ahead poniter n+1 time forward the move both pointers
        forward until ahead poniter is out of bound 
        then skip the node in front of the bofore coz thts our target node
        return dummy.next
        '''

        for m in range(n+1):
            ahead = ahead.next
        
        while ahead:
            ahead = ahead.next
            before = before.next

        before.next = before.next.next
        return dummy.next

    