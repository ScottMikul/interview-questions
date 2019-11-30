# Definition for singly-linked list.
import math
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check for either to to be entered as an empty listnode
        if l1.val is None or l2.val is None:
            if l1.val is None:
                l1.val = 0
            if l2.val is None:
                l2.val = 0

        d = math.floor((l1.val+l2.val)%10)
        #just makes more sense for carryover variable to be named c haha
        c = math.floor((l1.val+l2.val)/10)

        ret = ListNode(int(d))
        e = ret
        l1 = l1.next
        l2 = l2.next
        if l1 is None and l2 is None:
            if c==1:
                ret.next = ListNode(1)
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)

            d = math.floor((l1.val+l2.val+c)%10)
            c = math.floor((l1.val+l2.val+c)/10)
            e.next = ListNode(int(d))
            l1 = l1.next
            l2 = l2.next
            e = e.next
 

        if c==1:
            e.next= ListNode(1)  
        return ret
        
#(2 -> 4 -> 3) + (5 -> 6 -> 4)
#2 + 9 -> 6  = 1 -> 7

l1 = ListNode(1)
#l1.next = ListNode(4)
#l1.next.next= ListNode(3)
l2 = ListNode(9)
l2.next = ListNode(9)
#l2.next.next= ListNode(4)

sol = Solution().addTwoNumbers(l1,l2)
while sol:
    print(sol.val)
    sol = sol.next