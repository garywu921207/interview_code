'''
双十一众多商品进行打折销售，小明想购买自己心仪的一些物品，但由于受购买资金限制，所以他决定 从众多心仪商品中购买三件，而且想尽可能的花完资金，现在请你设计一个程序帮助小明计算尽可能花 费的最大资金数额。
输入描述: 输入第一行为一维整型数组M，数组长度小于100，数组元素记录单个商品的价格，单个商品价格小于 1000。
输入第二行为购买资金的额度R，R小于100000。 输出描述:
输出为满足上述条件的最大花费额度。 注意:如果不存在满足上述条件的商品，请返回-1。 示例1
输入
23,26,36,27 78
输出
76
说明 金额23、26和27相加得到76，而且最接近且小于输入金额78 示例2
输入
23,30,40
26
输出
-1
说明 因为输入的商品，无法组合出来满足三件之和小于26.故返回-1 备注:
输入格式是正确的，无需考虑格式错误的情况。
'''

#读取数据
import sys
if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    lst = list(map(int, line.split(',')))
    target = int(sys.stdin.readline().strip())
    n = len(lst)
    #if len(lst) < 3: print(-1) max_amount = 0
    max_amount = 0
    for first in range(n-2):
        for second in range(first+1, n-1):
            for third in range(second+1, n):
                curr_amount = lst[first]+lst[second]+lst[third]
                if curr_amount <= target:
                    max_amount = max(max_amount,curr_amount)
    if max_amount == 0:
        print(-1)
    else:
        print(max_amount)
