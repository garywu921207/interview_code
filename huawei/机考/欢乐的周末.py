'''
欢乐的周末
标题:欢乐的周末 | 时间限制:1秒 | 内存限制:262144K | 语言限制:不限
小华和小为是很要好的朋友，他们约定周末一起吃饭。通过手机交流，他们在地图上选择了多个聚餐地 点(由于自然地形等原因，部分聚餐地点不可达)，求小华和小为都能到达的聚餐地点有多少个? 输入描述:
第一行输入m和n，m代表地图的长度，n代表地图的宽度。 第二行开始具体输入地图信息，地图信息包含:
0 为通畅的道路
1 为障碍物(且仅1为障碍物)
2 为小华或者小为，地图中必定有且仅有2个 (非障碍物)
3 为被选中的聚餐地点(非障碍物)
输出描述:
可以被两方都到达的聚餐地点数量，行末无空格。

示例1
输入: 44
2 1 0 3
0 1 2 1
0 3 0 0
0 0 0 0
输出
2
说明:
    第一行输入地图的长宽为3和4。 第二行开始为具体的地图，
    其中:3代表小华和小明选择的聚餐地点;
    2代表小华或者小明(确保有2 个);
    0代表可以通行的位置;
    1代表不可以通行的位置。
    此时两者能都能到达的聚餐位置有2处

示例2
输入
44
2 1 2 3
0 1 0 0
0 1 0 0
0 1 0 0 输出
0
说明
第一行输入地图的长宽为4和4。
第二行开始为具体的地图，
其中:3代表小华和小明选择的聚餐地点;2代表小华或者小明(确保有2 个);
0代表可以通行的位置;
1代表不可以通行的位置。
由于图中小华和小为之间有个阻隔，此时，没有两人都能到达的聚餐地址，故而返回0
备注:
地图的长宽为m和n，其中:
4 <= m <= 100
4 <= n <= 100
聚餐的地点数量为 k，则
1< k <= 100
'''


class Mmap():
    def __init__(self, m):
        self.m = m

    def gogo(self, x, y):
        if x > 0 and self.m[x - 1][y] != 1 and self.m[x - 1][y] != 5:
            self.m[x - 1][y] = 5
            self.gogo(x - 1, y)
        if x < len(self.m) - 1 and self.m[x + 1][y] != 1 and self.m[x + 1][y] != 5:
            self.m[x + 1][y] = 5
            self.gogo(x + 1, y)
        if y > 0 and self.m[x][y - 1] != 1 and self.m[x][y - 1] != 5:
            self.m[x][y - 1] = 5
            self.gogo(x, y - 1)
        if y < len(self.m[x]) - 1 and self.m[x][y + 1] != 1 and self.m[x][y + 1] != 5:
            self.m[x][y + 1] = 5
            self.gogo(x, y + 1)


def inputV():
    m, n = input().split()
    m = int(m)
    n = int(n)
    xlocate = list()
    ylocate = list()
    mm = list()
    mm1 = list()
    for i in range(m):
        mm.append([])
        mm1.append([])
        aa = (input().split())
        for q in range(n):
            # mm[i,q]=aa[q]
            if int(aa[q]) == 2:
                xlocate.append([i, q])
                mm[i].append(0)
                mm1[i].append(0)
            elif int(aa[q]) == 1:
                mm[i].append(1)
                mm1[i].append(1)
            elif int(aa[q]) == 3:
                ylocate.append([i, q])
                mm[i].append(0)
                mm1[i].append(0)
            elif int(aa[q]) == 0:
                mm[i].append(0)
                mm1[i].append(0)

    mmap1= Mmap(mm)
    mmap1.gogo(xlocate[0][0],xlocate[0][1])

    mmap2= Mmap(mm1)
    mmap2.gogo(xlocate[1][0],xlocate[1][1])
    counter = 0
    for i in range(len(ylocate)):
        if mmap1.m[ylocate[i][0]][ylocate[i][1]] == 5 and mmap2.m[ylocate[i][0]][ylocate[i][1]] == 5 :
            counter = counter +1

    return counter

while True:
    try:
        print(inputV())
    except:
        break
