import numpy as np

np.random.seed(42)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 数据，4个样本，每个2维输入
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([
    [0],
    [1],
    [1],
    [0]
])

n_samples = X.shape[0] # 4
n_features = X.shape[1] # 2
n_hidden = 2 # 隐藏层神经元个数


# 网络结构 2-2-1

w1 = np.random.uniform(-1, 1, (n_hidden, n_features))
# 广播机制，自动扩展维度
b1 = np.random.uniform(-1, 1, (n_hidden, 1))
w2 = np.random.uniform(-1, 1, (1, n_hidden))
b2 = np.random.uniform(-1, 1, (1, 1))

lr = 0.5


for epoch in range(10000):
    # 前向传播
    Z1 = w1 @ X.T + b1 # 2x4
    H1 = sigmoid(Z1)

    Z2 = w2 @ H1 + b2 # 1x4
    Y_hat = sigmoid(Z2)

    # 计算损失
    loss = np.mean((Y_hat - Y.T) ** 2)

    # 反向传播
    dZ2 = 2 * (Y_hat - Y.T) * Y_hat * (1 - Y_hat) # 1x4
    dw2 = dZ2 @ H1.T # 1x4 * 4x2 = 1x2 和 w2 的形状一样
    # axis=1 表示按行求和，keepdims=True 表示保持维度
    db2 = np.sum(dZ2, axis=1, keepdims=True)

    # 隐藏层
    dH1 = w2.T @ dZ2 # 2x1 * 1x4 = 2x4
    dZ1 = dH1 * H1 * (1 - H1) # 2x4
    dw1 = dZ1 @ X # 2x4 * 4x2 = 2x2 和 w1 的形状一样
    db1 = np.sum(dZ1, axis=1, keepdims=True)

    # 更新参数
    w2 -= lr * dw2 / n_samples
    b2 -= lr * db2 / n_samples
    w1 -= lr * dw1 / n_samples
    b1 -= lr * db1 / n_samples

    if epoch % 1000 == 0:
        print(f'Epoch {epoch}, Loss: {loss}')

# 预测
print("\n预测对比：")
print(f"{'x1':>4} {'x2':>4} {'真实y':>8} {'预测y':>10}")

Z1 = w1 @ X.T + b1
H1 = sigmoid(Z1)
Z2 = w2 @ H1 + b2
Y_hat = sigmoid(Z2)

for i in range(n_samples):
    x1, x2 = X[i]
    real = Y[i][0]
    pred = Y_hat[0][i]
    print(f"{x1:>4} {x2:>4} {real:>8} {pred:>10.4f}")



