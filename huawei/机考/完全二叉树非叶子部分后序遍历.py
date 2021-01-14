'''
标题:完全二叉树非叶子部分后序遍历 | 时间限制:1秒 | 内存限制:262144K | 语言限制:不限
给定一个以顺序储存结构存储整数值的完全二叉树序列(最多1000个整数)，请找出此完全二叉树 的所有非叶子节点部分，然后采用后序遍历方式将此部分树(不包含叶子)输出。
1、只有一个节点的树，此节点认定为根节点(非叶子)。 2、此完全二叉树并非满二叉树，可能存在倒数第二层出现叶子或者无右叶子的情况
其他说明:二叉树的后序遍历是基于根来说的，遍历顺序为:左-右-根 输入描述:
一个通过空格分割的整数序列字符串
输出描述:
非叶子部分树结构的后序遍历结果 示例1
输入
1 2 3 4 5 6 7
输出
2 3 1
说明 找到非叶子部分树结构，然后采用后续遍历输出
备注: 输出数字以空格分隔
'''
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def Create_tree(root, val):
    newnode = TreeNode(val)
    newnode.left = None
    newnode.right = None
    if root == None:
        root = newnode
        return root
    else:
        current = root
        while current != None:
            backup = current
            if current.val > val:
                current = current.left
            else:
                current = current.right
        if backup.val > val:
            backup.left = newnode
        else:
            backup.right = newnode
        return root

def postorder(ptr):
    if ptr != None:
        postorder(ptr.left)
        postorder(ptr.right)
        #if ptr.left != None and ptr.right != None:
        #print(ptr.val,end=' ')
        print(ptr.val,end=' ')

if __name__ == '__main__':
    data = list(map(int,input().split()))
    if len(data) == 1:
        print(data[0])
    else:
        ptr = None
        for i in range(len(data)):
            ptr = Create_tree(ptr,data[i])
        postorder(ptr)
