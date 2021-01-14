'''
小明负责公司年会，想出一个趣味游戏: 屏幕给出1~9中任意3个不重复的数字，大家以最快时间给出这几个数字可拼成的数字从小到大排列位
于第N位置的数字，其中N为给出的数字中最大的(如果不到这么多个数字则给出最后一个即可)。 注意:
1)2可以当做5来使用，5也可以当做2来使用进行数字拼接，且屏幕不能同时给出2和5; 2)6可以当做9来使用，9也可以当做6来使用进行数字拼接，且屏幕不能同时给出6和9。
如给出:1，4，8，则可以拼成的数字为: 1，4，8，14，18，41，48，81，84，148，184，418，481，814，841 那么最第N(即8)个的数字为81。
输入描述:
输入为以逗号分隔的描述3个int类型整数的字符串。
输出描述: 输出为这几个数字可拼成的数字从小到大排列位于第N(N为输入数字中最大的数字)位置的数字，如果 输入的数字不在范围内或者有重复，则输出-1。
示例1
输入
1,4,8
输出
81
说明
可以构成的数字按从小到大排序为1，4，8，14，18，41，48，81，84，148，184，418，481， 814，841，故第8个为81
示例2
输入
2,5,1
输出
-1
说明
2和5不能同时出现
示例3
输入
3,0,9
输出
-1
说明
0不在1到9的范围内
示例4
输入
3,9,7
输出
67
说明 注意9可以当6使用，所以可以构成的数字按从小到大排序为3，6，7，9，36，37，39，63，67，73， 76，79，93，97...(省略后面的数字)，故第9个为67
'''

import sys

try:
    num = [int(val) for val in sys.stdin.readline()[:-1].split(',')]
except:
    print(-1)
    exit()
check = set()

for i in num:
    if i < 1 or i > 9:
        print(-1)
        exit()
    check.add(i)
if len(check) != 3:
    print(-1)
    exit()
if (2 in check and 5 in check) or (6 in check and 9 in check):
    print(-1)
    exit()

for i in num:
    if i == 2:
        num.append(5)
    if i == 5:
        num.append(2)
    if i == 6:
        num.append(9)
    if i == 9:
        num.append(6)
num.sort()
n = num[-1] - 1

def dfs(rem, pre):
    if not rem:
        return pre
    re = set()
    for i in rem:
        newstack = [val * 10 + i for val in pre]
        newstack.append(i)
        sets = rem.copy()
        sets.remove(i)
        re.update(dfs(sets, newstack))
        #re+=dfs(sets,pre)
    return re

#print(set(num))
stack=dfs(set(num),[])
print(stack, "++++++")
stack=list(stack)
stack.sort()
#print(stack)
print(stack[n])
