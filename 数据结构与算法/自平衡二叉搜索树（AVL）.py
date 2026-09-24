"""
左旋
目标：右边太高，把右孩子 y 提上来当根。
约束：BST 要求“左小右大”，且中序顺序不能变。
推导：
    y 当根，左边必须是比 y 小的：也就是 x 和 T2。
    又因为 x < T2（原来在 BST 里的位置），所以 x 只能当 y 的左孩子。
    T2 比 x 大，所以 T2 只能当 x 的右孩子。
    z 比 y 大，继续当 y 的右孩子。
结果：指针这么一改，就是代码里的左旋。


AVL = BST + 高度 + 旋转 + 自平衡。插入时沿路径回溯，遇到不平衡就旋转。旋转是“改形状”和“降高度”的组合，保证既平衡又满足 BST。

左子树不平衡，且插入到左子树的左边，需要左旋（LL）。
右子树不平衡，且插入到右子树的右边，需要右旋（RR）。

左子树不平衡，且插入到左子树的右边，需要左子树左旋后根节点右旋（LR）。
右子树不平衡，且插入到右子树的左边，需要右子树右旋后根节点左旋（RL）。


"""

# 自平衡二叉搜索树
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1         # 新节点高度默认为1

# 获取高度
def get_height(node):
    if node is None:
        return 0
    return node.height


# 更新节点高度
def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))  # 获取左右子树高度的最大值，并加1

# 平衡因子
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


# 右旋
def rotate_right(y):
    x = y.left              # x 是 y 的左孩子
    T2 = x.right            # T2 是 x 的右孩子

    x.right = y             # 符合 BST 要求，x 的右孩子是 y
    y.left = T2             # 符合 BST 要求，y 的左孩子是 T2

    update_height(y)
    update_height(x)

    return x                # 返回 x 作为新的根节点

# 左旋
def rotate_left(x):
    y = x.right             # y 是 x 的右孩子
    T2 = y.left             # T2 是 y 的左孩子

    y.left = x              # 符合 BST 要求，y 的左孩子是 x
    x.right = T2            # 符合 BST 要求，x 的右孩子是 T2

    update_height(x)
    update_height(y)

    return y                # 返回 y 作为新的根节点

# 插入操作，逐层回溯，左旋右旋操作调节高度，保持 AVL 树平衡
def insert(node, data):
    # 1. 普通BST插入
    if node is None:
        return AVLNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:
        return node         # 数据已存在，不重复插入

    # 2. 更新节点高度
    update_height(node)

    # 3. 计算平衡因子
    balance = get_balance(node)

    # 4. 判断四种不平衡的情况
    # LL: 左边高，且插入到左子树的左边，导致左子树不平衡
    if balance > 1 and data < node.left.data:
        return rotate_right(node)

    # RR: 右边高，且插入到右子树的右边，导致右子树不平衡
    if balance < -1 and data > node.right.data:
        return rotate_left(node)

    # LR: 左边高，且插入到左子树的右边，导致左子树不平衡
    if balance > 1 and data > node.left.data:    # 左边高，且左子树的高度集中于右边
        node.left = rotate_left(node.left)       # 左旋左子树，使左子树高度平衡
        return rotate_right(node)                # 右旋自己，使自己高度平衡

    # RL: 右边高，且插入到右子树的左边，导致右子树不平衡
    if balance < -1 and data < node.right.data:
        node.right = rotate_right(node.right)     # 右旋右子树
        return rotate_left(node)                  # 左旋自己

    # 5. 平衡，直接返回
    return node

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

# 删除操作
def delete(node, data):
    if node is None:
        return None

    # 1. 普通BST删除
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:           # 找到要删除的节点
        if node.left is None:           # 如果左子树为空
            return node.right           # 返回右子树作为新的根节点
        elif node.right is None:        # 如果右子树为空
            return node.left            # 返回左子树作为新的根节点
        successor = find_min(node.right)                               # 找到右子树的最小节点
        node.data = successor.data                                     # 将最小节点的值赋给当前节点
        node.right = delete(node.right, successor.data)     # 递归删除右子树的最小节点

    # 2. 更新节点高度
    update_height(node)

    # 3. 计算平衡因子
    balance = get_balance(node)

    # 4. 判断四种不平衡的情况
    # LL: 删除后，左边高，且左子树的左边不平衡，需要左旋（LL）
    if balance > 1 and get_balance(node.left) >= 0:
        return rotate_right(node)

    # LR: 删除后，左边高，且左子树的右边不平衡，需要左子树左旋后根节点右旋（LR）
    if balance > 1 and get_balance(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    # RR: 删除后，右边高，且右子树的右边不平衡，需要右旋（RR）
    if balance < -1 and get_balance(node.right) <= 0:
        return rotate_left(node)

    # RL: 删除后，右边高，且右子树的左边不平衡，需要右子树右旋后根节点左旋（RL）
    if balance < -1 and get_balance(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node


# 中序遍历
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=",")
    inorder(node.right)

# 打印树结构
def print_tree(node, level=0, prefix="根节点: "):
    if node is not None:
        bf = get_balance(node)
        print(" " * (level * 4) + prefix +
              f"{node.data} (h={node.height}, bf={bf})")
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")



if __name__ == "__main__":
    root = None
    for x in [10, 20,21,22,23, 30, 40, 50, 25]:
        root = insert(root, x)

    print("插入操作后，树结构:")
    print_tree(root)
    print("中序遍历（应该有序）:")
    inorder(root)
    print("\n")

    print("删除操作后，树结构:")
    root = delete(root, 10)
    root = delete(root, 21)
    print_tree(root)
    print("中序遍历（应该有序）:")
    inorder(root)
    print("\n")
