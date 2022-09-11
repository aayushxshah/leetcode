#https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

xlist1 = [1,2,4]
xlist2 = [1,3,4]

def creatList (l):
    head = ListNode(l[0])
    itr = head
    for i in l[1:]:
        while itr.next:
            itr = itr.next
        itr.next = ListNode(i)
    return head

def llprint (head):
    itr = head
    while itr.val:
        print(itr.val)
        itr = itr.next

list1 = None#creatList(xlist1)
list2 = ListNode()#creatList(xlist2)

class Solution:

    def compare (self,prev,node1,node2):
        if node1 == None:
            prev.next = node2
            return
        elif node2 == None:
            prev.next = node1
            return

        if node1.val <= node2.val:
            prev.next = ListNode(node1.val)
            self.compare(prev.next,node1.next,node2)
        else: 
            prev.next = ListNode(node2.val)
            self.compare(prev.next,node1,node2.next)
        

    def mergeTwoLists(self, list1, list2):

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            self.head = ListNode(list1.val)
            self.compare(self.head,list1.next,list2)
        else:
            self.head = ListNode(list2.val)
            self.compare(self.head,list1,list2.next)
        return self.head


s = Solution()
start = s.mergeTwoLists(list1,list2)
print(start)
        

