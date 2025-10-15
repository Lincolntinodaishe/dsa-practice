# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #create a fake node
        curr = dummy # your pointer assign it to the first node 
        while list1 and list2: # while the lists are still valid merge the node with the least value to the the new list with the dummy head
            if list1.val < list2.val: # if statmnt we want to check the value in each list we use .val
                curr.next = list1 # make it the next node
                list1 = list1.next # move to the next node in the specific list
            else: 
                curr.next = list2  
                list2 = list2.next
            curr = curr.next # when you add the least node form the lists we want to update the curr in the final linked list with in the loop
        # if we have remainders in either of the list we want to connect them to the final linkdlist 
        # so we check if the list is valid and we connect its first node which connects the rest
        if list1:  
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next     # return everything after the dummy