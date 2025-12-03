# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        #iterate through each and evry value in the linked list
        #convert at evry step by using the fommular answer*2 + head.val
        #return answer
        answer = 0
        while head:
            answer = answer*2 + head.val
            head = head.next
        return answer