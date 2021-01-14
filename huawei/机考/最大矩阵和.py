'''
给定一个二维整数矩阵，要在这个矩阵中选出一个子矩阵，使得这个子矩阵内所有的数字和尽量大，我 们把这个子矩阵称为和最大子矩阵，子矩阵的选取原则是原矩阵中一块相互连续的矩形区域。
输入描述:
输入的第一行包含2个整数n, m(1 <= n, m <= 10)，表示一个n行m列的矩阵，下面有n行，每行有m个整 数，同一行中，每2个数字之间有1个空格，最后一个数字后面没有空格，所有的数字的在[-1000, 1000] 之间。
输出描述: 输出一行一个数字，表示选出的和最大子矩阵内所有的数字和。 示例1
输入
34
-3 5 -1 5
2 4 -2 4
-1 3 -1 3
输出
20
说明
一个3*4的矩阵中， 后面3列的子矩阵求和加起来等于20，和最大。
'''
while True:
    try:
        s = list(map(int,input().split()))
        n = s[0]
        m = s[1]
        array = [[0]*m for _ in range(n)]
        for i in range(n):
            line = list(map(int,input().split()))
            for j in range(m):
                array[i][j] = line[j]
        max = -999999
        for i in range(1,n+1):
            for j in range(1,m+1):
                for ii in range(n-i+1):
                    for jj in range(m-j+1):
                        sub = [[0] * j for _ in range(i)]
                        for subi in range(i):
                            for subj in range(j):
                                sub[subi][subj] += array[ii+subi][jj+subj]
                        c = 0
                        for p in range(len(sub)):
                            for q in range(len(sub[0])):
                                c +=sub[p][q]
                        if c>max:
                            max = c
        print(max)
    except:
        break
