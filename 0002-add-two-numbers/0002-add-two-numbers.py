# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Helper function to convert a linked list into an array of its values
        def lltoarr(head):
            arr = []
            curr = head
            # Traverse the list and append node values into the array
            while curr:
                arr.append(curr.val)
                curr = curr.next
            return arr
        # Convert both linked lists into arrays
        arr1 = lltoarr(l1)
        arr2 = lltoarr(l2)
        arr3 = []
        # Reverse both arrays, join digits into strings, convert to ints, and add them
    # Example: [2,4,3] → "342"
        res = int(''.join (map (str, arr1[::-1]))) + int(''.join(map ( str,arr2[::-1])))
        # append to arr3 and reverse it since the final LL is the reversal of this
        for i in str(res):
            arr3.append(int(i))
        arr3 = arr3[::-1]
        # Helper function to convert an array back into a linked list
        def arrtoll(arr):
            # if our array is empty return none
            if not arr:
                return None
            # assign the head to be the first number
            head = ListNode(arr[0])
            curr = head
            for i in arr[1:]:
                # create a node for each number and move to the next
                curr.next =ListNode(i)
                curr = curr.next
            # return the head of the list
            return head
        # cal your function to convert
        return arrtoll(arr3) 


            
        