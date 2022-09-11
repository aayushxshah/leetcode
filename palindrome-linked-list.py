#https://leetcode.com/problems/palindrome-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

xhead = [1]


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

head = creatList(xhead)

class Solution:
    def isPalindrome(self, head) -> bool:
        llist = []
        itr = head
        while itr != None:
            llist.append(itr.val)
            itr = itr.next
        
        if len(llist)%2 == 1:
            llist.pop(len(llist)%2)
        
        if len(llist) == 0:
            return True

        x = int(len(llist)/2)
        reversed = llist[x:]
        reversed = reversed[::-1]

        i = 0
        for j in reversed:
            if j != llist[i]:
                return False
            i += 1

        return True

s = Solution()
print(s.isPalindrome(head))