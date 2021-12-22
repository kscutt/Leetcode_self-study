# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None  # Initially theres no prev nodes bc we're at the beninging
	        current = head # gonna rename the head as current 
        
        while current is not None:  # while there are nodes      
            nextnode = current.next # move the next pointer over
		        current.next = prev     # this is what reverses the arrows
            prev = current          # move previous over 
            current = nextnode      # move current over
            
        return prev # eventually previous will be at the head of the reversed list
