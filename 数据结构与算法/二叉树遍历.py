

# 二叉树
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


# 前序遍历
def preorder(node):
    if node is None:
        return
    print(node.data, end="")
    preorder(node.left)
    preorder(node.right)


# 中序遍历
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end="")
    inorder(node.right)


# 后序遍历
def postorder(node):
    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.data, end="")



a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

a.left = b
a.right = c
b.left = d
b.right = e

print("前序遍历: ", end="")
preorder(a)
print()

print("中序遍历: ", end="")
inorder(a)
print()

print("后序遍历: ", end="")
postorder(a)
print()
