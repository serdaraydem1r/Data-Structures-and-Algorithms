class Solution:
    def removeNthFromEnd(self,head,n):
        leftPointer = head
        rightPointer = head

        while n>0 and rightPointer:
            rightPointer = rightPointer.next
            n -= 1
        while rightPointer and rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next
        if leftPointer == head and not rightPointer:
            return head.next
        leftPointer.next = leftPointer.next.next
        return head