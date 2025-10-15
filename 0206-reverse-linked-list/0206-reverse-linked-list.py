# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers fisrt one points to null before the head and the second one to the head
        prev = None
        curr = head
        # want to traverse through out my loop untill my curr doent exist we us while loop
        while curr:
            # store the next node in a variable
            nxt = curr.next 
            curr.next = prev #the arrow of the current nodes now point to the prev which is the null in the first loop
            prev = curr # move the prev to be the curr node which is the head in the first loop
            curr = nxt # move the curr node tobe the next one which is the head to be the next node
        return prev # at the end of the loop prev will be my last node which will be my head at that point