# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head.next
        while f and f.next:
            f = f.next.next
            s = s.next
        sec = s.next
        s.next = prev = None
        while sec:
            nxt = sec.next
            sec.next = prev
            prev = sec
            sec = nxt
        
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
