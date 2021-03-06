'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

'''
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    '''
    思路 感觉链表的题是有模版和套路啊～！
    首先创建一个头节点及一个哨兵节点，头节点作为新链表的头节点，然后用一个哨兵节点对链表进行操作，
    就拿此题来说，套用以上模版+处理其他情况(考虑代码鲁棒性)
    step1: create sential_node+dummy_node
    step2: 开始while l1&l2
    step3: 相同位相加 干就完了
    step4: 考虑两个其他情况: 1长度不相等 2：有进位的情况
    step5: 不停的next 直到l1 or l2射没了....
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个结点值为 None 的头结点, dummy 和 p 指向头结点, dummy 用来最后返回, p 用来遍历
        dummy = p = ListNode(None)
        s = 0  # 初始化进位 s 为 0
        while l1 or l2 or s:
            # 如果 l1 或 l2 存在, 则取l1的值 + l2的值 + s(s初始为0, 如果下面有进位1, 下次加上)
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)  # p.next 指向新链表, 用来创建一个新的链表
            p = p.next  # p 向后遍历
            s //= 10  # 有进位情况则取模, eg. s = 18, 18 // 10 = 1
            l1 = l1.next if l1 else None  # 如果l1存在, 则向后遍历, 否则为 None
            l2 = l2.next if l2 else None  # 如果l2存在, 则向后遍历, 否则为 None
        return dummy.next  # 返回 dummy 的下一个节点, 因为 dummy 指向的是空的头结点, 下一个节点才是新建链表的后序节点

class Solution2:
    '''投机取巧法: 做一个字符串和整数的映射, 然后对每一位进行加总'''
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5': 5, '6':6, '7':7, '8':8, '9':9}
        res = 0
        for index, string in enumerate(num1[::-1]):
            res += dic[string] * (10 ** index)

        for index, string in enumerate(num2[::-1]):
            res += dic[string] * (10 ** index)
        return str(res)
