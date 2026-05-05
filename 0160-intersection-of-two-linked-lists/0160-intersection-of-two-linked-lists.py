# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next
        if headA == headB:
            return headA
        curra, currb = headA, headB
        if lenA > lenB:
            diff = lenA-lenB
            while diff:
                curra = curra.next
                diff -= 1
        if lenB > lenA:
            diff = lenB-lenA
            while (diff):
                currb = currb.next
                diff -= 1
        while curra and currb:
            if curra == currb:
                return curra
            curra = curra.next
            currb = currb.next
        return  None
        


        