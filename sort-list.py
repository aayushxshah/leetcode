#https://leetcode.com/problems/sort-list/
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def creatList (l):
    head = ListNode(l[0])
    itr = head
    for i in l[1:]:
        while itr.next:
            itr = itr.next
        itr.next = ListNode(i)
    return head
def lenList (head):
    i = 0
    itr = head
    while itr:
        i += 1
        itr = itr.next
    return i

head = creatList([-1,5,3,4,0])

class Solution:
    def sortList(self, head):

        length = lenList(head)
        mid = length // 2

        

