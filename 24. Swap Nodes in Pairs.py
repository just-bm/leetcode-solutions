# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        odd = ListNode()
        even = ListNode()
        odd_curr = odd
        even_curr = even

        index = 1
        while temp:
            if index % 2 == 0:
                even_curr.next = ListNode(temp.val)
                even_curr = even_curr.next
                temp = temp.next
            elif index % 2 == 1:
                odd_curr.next = ListNode(temp.val)
                odd_curr = odd_curr.next
                temp = temp.next
            index +=  1
        odd = odd.next
        even = even.next

        odd_pointer = odd
        even_pointer = even

        res = ListNode()
        curr = res
        n = 1
        print(index)
        while n < index:
            curr.next = ListNode(-1)
            n += 1
            curr = curr.next
        

        odd_p = odd
        even_p = even
        even_num = 0
        odd_num = 0
        curr = res
        while odd_p or even_p:
            if even_p:
                curr.next = ListNode(even_p.val)
                curr = curr.next
                even_p = even_p.next
                even_num += 1
            if odd_p:
                curr.next = ListNode(odd_p.val)
                curr = curr.next
                odd_p = odd_p.next
                
        return res.next
