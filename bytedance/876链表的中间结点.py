
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class Solution2:
    '''
    思路和算法
    链表的缺点在于不能通过下标访问对应的元素。因此我们可以考虑对链表进行遍历，
    同时将遍历到的元素依次放入数组 A 中。
    如果我们遍历到了 N 个元素，那么链表以及数组的长度也为 N，对应的中间节点即为 A[N/2]。

    '''
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]
