# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1, p2 = l1, l2
        l3 = None
        t3 = None
        c = 0
        while p1 or p2:
            if p1 and p2:
                node = ListNode((p1.val+p2.val+c)%10)
                c = 1 if (p1.val+p2.val+c) >= 10 else 0
                if not l3:
                    l3 = node
                    t3 = node
                else:
                    t3.next = node 
                    t3 = t3.next
                p1 = p1.next
                p2 = p2.next
            if p1 and not p2:
                node = ListNode((p1.val+c)%10)
                c = 1 if (p1.val+c) >= 10 else 0
                if not l3:
                    l3 = node
                    t3 = node
                else: 
                    t3.next = node 
                    t3 = t3.next
                p1 = p1.next
            if p2 and not p1:
                node = ListNode((p2.val+c)%10)
                c = 1 if (p2.val+c) >= 10 else 0
                if not l3:
                    l3 = node
                    t3 = node
                else:
                    t3.next = node 
                    t3 = t3.next
                p2 = p2.next
        if c:
            node = ListNode(c)
            t3.next = node 
            t3 = t3.next
        return l3
