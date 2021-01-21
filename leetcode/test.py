class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def twoMergeList(s1, s2):
    '''
    '''
    dummy = p = ListNode(None)
    while s1 or s2:
        if s1.val < s2.val:
            p = s1.val
            s1 = s1.next
        else:
            p = s2.val
            s2 = s2.next
        p = p.next
    p.next = s1 or s2
    return dummy.next
