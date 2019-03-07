# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry=0
        res=[]
        while True:
            l1_val = l1.val if l1!=None else 0
            l2_val = l2.val if l2!=None else 0
            total = l1_val + l2_val + carry
            carry = total//10
            remain = total%10
            res.append(remain)
            
            l1 = l1.next if l1!=None else None
            l2 = l2.next if l2!=None else None
            if (l1==None) and (l2==None):
                break
        if carry !=0:
            res.append(carry)
            
        return res
