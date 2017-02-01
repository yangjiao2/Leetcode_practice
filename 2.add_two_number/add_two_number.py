# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sol = ListNode(0)
        head = sol
        
        carry = 0
        while(l1 != None or l2 != None or carry  != 0):
            if (l1 == None and l2 == None):
                curr = carry % 10
                carry = carry / 10
            elif (l1 == None):
                curr = (l2.val + carry) % 10
                carry = (l2.val + carry) / 10
            elif (l2 == None):
                curr = (l1.val + carry) % 10
                carry = (l1.val + carry) / 10
            
            else:
                curr = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) / 10
            
            head.next = ListNode(curr)
            head = head.next
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        
        return sol.next


"""
1st fail:
did not link 1st to 2nd node because the second loop could not link 2nd node back to 1st node
solve it could be create a fake first node and return first.next

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carryon = 0;
        ListNode result = null;
        ListNode head = result;
        while(l1 != null || l2 != null){
            int node1 = (l1 == null? 0 : l1.val);
            int node2 = (l2 == null? 0 : l2.val);
            if (result == null){
                result = new ListNode((node1 + node2 + carryon) / 10);
            }else{
                result.next = new ListNode((node1 + node2 + carryon)/10);
            }
            carryon = (node1 + node2) % 10;
            l1 = (l1 == null? null: l1.next);
            l2 = (l2 == null? null: l2.next);
            result = result.next;
        }
        return result;
    }
}


2nd fail: did not move node forward

3rd fail: line 35 and line 37, should always check if nodes have next 
    example case:
        [5]
        [5]


"""