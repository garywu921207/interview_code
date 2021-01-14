class Solution:
    '''投机取巧法😄'''
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        res = 0
        for index, string in enumerate(num1[::-1]):
            res += dic[string] * (10 ** index)

        for index, string in enumerate(num2[::-1]):
            res += dic[string] * (10 ** index)
        return str(res)




class Solution2:
    '''双指针法'''
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
