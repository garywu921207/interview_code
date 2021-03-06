'''
有一个考古学家发现一个石碑，但是很可惜，发现时其已经断成多段，原地发现n个断口整齐的石碑碎 片。为了破解石碑内容，考古学家希望有程序能帮忙计算复原后的石碑文字组合数，你能帮忙吗? 输入描述:
第一行输入n，n表示石碑碎片的个数。
第二行依次输入石碑碎片上的文字内容s，共有n组。 输出描述: 输出石碑文字的组合(按照升序排列)，行末无多余空格。 示例1
输入
3
a bc
输出
abc
acb
bac
bca
cab
cba
说明 当石碑碎片上的内容为“a”，“b”，“c”时，则组合有“abc”，“acb”，“bac”，“bca”，“cab”，“cba” 示例2
输入
3
a ba
输出
aab
aba
baa
说明
当石碑碎片上的内容为“a”，“b”，“a”时，则可能的组合有“aab”，“aba”，“baa”
示例3
输入
3
a b ab
输出
aabb
abab
abba
baab
baba
说明 当石碑碎片上的内容为“a”，“b”，“ab”时，则可能的组合有“aabb”，“abab”，“abba”，“baab”，“baba” 备注: 如果存在石碑碎片内容完全相同，则由于碎片间的顺序变换不影响复原后的碑文内容，即相同碎片间的 位置变换不影响组合。
'''
import itertools
n = int(input().strip())
sp = input().split()

multi = itertools.permutations(sp)
result = set(list(map(lambda t: ''.join(t), multi)))
for item in result:
    print(item)
