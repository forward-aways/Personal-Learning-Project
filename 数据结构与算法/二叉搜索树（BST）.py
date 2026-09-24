

# 二叉搜索树
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 搜索
def search(node, target):
    if node is None:
        return False

    if node.data == target:      # 找到目标节点
        return True

    if target < node.data:                                # 目标值小于当前节点值，搜索左子树
        return search(node.left, target)      # 递归搜索左子树
    else:                                                 # 目标值大于当前节点值，搜索右子树
        return search(node.right, target)     # 递归搜索右子树

# 插入
def insert(node, data):
    if node is None:                                      # 当前节点为空，插入新节点
        return TreeNode(data)

    if data < node.data:                                  # 数据小于当前节点数据，插入左子树
        node.left = insert(node.left, data)    # 递归插入左子树
    elif data > node.data:                                # 数据大于当前节点数据，插入右子树
        node.right = insert(node.right, data)  # 递归插入右子树

    return node

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

# 删除
def delete(node, data):
    if node is None:
        return None

    if data < node.data:
        node.left = delete(node.left, data)         # 数据小于当前节点数据，删除左子树
    elif data > node.data:
        node.right = delete(node.right, data)       # 数据大于当前节点数据，删除右子树
    else:                                   # 找到目标节点
        if node.left is None:
            return node.right               # 左子树为空，返回右子树
        elif node.right is None:
            return node.left                # 右子树为空，返回左子树
        # 找到右子树的最小节点，该节点符合BST性质，用于替换当前节点
        successor = find_min(node.right)          # 找到右子树的最小节点
        node.data = successor.data                # 将最小节点的值赋给当前节点
        node.right = delete(node.right, successor.data)  # 递归删除右子树的最小节点

    return node



def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end=",")
    inorder(node.right)



# 构建BST
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

# 中序遍历
print("中序遍历: ", end="")
inorder(root)
print()

# 搜索
print("搜索结果: ", search(root, 6))
print("搜索结果: ", search(root, 11))
print("搜索结果: ", search(root, 14))




