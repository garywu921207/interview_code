class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = p = ListNode(None)
    s = 0
    while l1 and l2:
        s += (l1.val if l1.val else 0) + (l2.val if l2.val else 0)
        p.next = ListNode(s % 10)
        p = p.next
        s //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
