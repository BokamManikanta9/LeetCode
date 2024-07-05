# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        c=head.next
        p=head.val
        l=[]
        l1=[]
        i=0
        while c.next!=None:
            if c.val>c.next.val and c.val>p:
                l.append(i)
            elif c.val<c.next.val and c.val<p:
                l.append(i)
            i+=1
            p=c.val
            c=c.next
        i=0
        j=1
        a=len(l)-1
        while a>0:
            l1.append(l[j]-l[i])
            i+=1
            j+=1
            a-=1
        if len(l1)<1:
            return [-1,-1]
        return [min(l1),(l[-1]-l[0])]
        