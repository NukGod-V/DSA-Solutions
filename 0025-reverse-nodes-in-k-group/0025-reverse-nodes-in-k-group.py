# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Dummy = ListNode(0, head)
        groupPrev = Dummy
        while True:
            KTH = self.KTHNode(groupPrev, k)
            if not KTH:
                break
            groupNext = KTH.next
            
            prev, curr = KTH.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = KTH
            groupPrev = temp
        
        return Dummy.next


    def KTHNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr