import numpy as np

np.random.seed(42)


# ============================================================
# 1. 线性层
# ============================================================
class Linear:
    def __init__(self, in_features, out_features):
        # 形状：(本层神经元数, 上一层输出数)
        self.W = np.random.uniform(-1, 1, (out_features, in_features))
        self.b = np.random.uniform(-1, 1, (out_features, 1))

    def forward(self, X):
        # X 形状：(in_features, n_samples)
        self.X = X                              # 存下来，反向要用
        return self.W @ X + self.b              # (out, n)

    def backward(self, dZ):
        # dZ 形状：(out_features, n_samples)
        self.dW = dZ @ self.X.T                 # (out, n) @ (n, in) = (out, in)
        self.db = np.sum(dZ, axis=1, keepdims=True)   # (out, 1)
        return self.W.T @ dZ                    # (in, n)，传给上一层

    def update(self, lr, n):
        self.W -= lr * self.dW / n
        self.b -= lr * self.db / n


# ============================================================
# 2. 激活函数
# ============================================================
class Sigmoid:
    def forward(self, Z):
        self.A = 1 / (1 + np.exp(-Z))
        return self.A

    def backward(self, dA):
        return dA * self.A * (1 - self.A)


class ReLU:
    def forward(self, Z):
        self.Z = Z
        return np.maximum(0, Z)

    def backward(self, dA):
        return dA * (self.Z > 0)


# ============================================================
# 3. 损失函数
# ============================================================
class MSELoss:
    def forward(self, y_hat, y):
        self.y_hat = y_hat
        self.y = y
        return np.mean((y_hat - y) ** 2)

    def backward(self):
        n = self.y.shape[1]
        return 2 * (self.y_hat - self.y) / n


# ============================================================
# 4. 网络：把层串起来
# ============================================================
class Network:
    def __init__(self, layers):
        self.layers = layers

    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def backward(self, dA):
        for layer in reversed(self.layers):    # 倒序
            dA = layer.backward(dA)

    def update(self, lr, n):
        for layer in self.layers:
            if hasattr(layer, 'update'):       # 只有 Linear 有 update
                layer.update(lr, n)


