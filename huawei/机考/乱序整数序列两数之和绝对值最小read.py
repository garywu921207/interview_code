'''
乱序整数序列两数之和绝对值最小
标题:乱序整数序列两数之和绝对值最小 | 时间限制:1秒 | 内存限制:262144K | 语言限制:不 限
给定一个随机的整数(可能存在正整数和负整数)数组 nums ，请你在该数组中找出两个数，其和的绝 对值(|nums[x]+nums[y]|)为最小值，并返回这个两个数(按从小到大返回)以及绝对值。
每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
输入描述:
一个通过空格分割的有序整数序列字符串，最多1000个整数，且整数数值范围是 [-65535, 65535]。 输出描述:
两数之和绝对值最小值 示例1
输入
-1 -3 7 5 11 15
输出
-3 5 2
说明
因为 |nums[0] + nums[2]| = |-3 + 5| = 2 最小，所以返回 -3 5 2
'''

while True:
    try:
        l = list(map(int, input().split()))
        l.sort()
        a = l[0]
        b = l[1]
        minsum = abs(l[0] + l[1])
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                if abs(l[i] + l[j]) < minsum:
                    a = l[i]
                    b = l[j]
                    minsum = abs(a + b)
        print(a, b, minsum)
    except:
        break
