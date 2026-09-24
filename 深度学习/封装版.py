import numpy as np
from network import Network, Linear, Sigmoid, MSELoss, ReLU

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])              # (4, 2)

Y = np.array([[0],
              [1],
              [1],
              [0]])                 # (4, 1)

# 统一转成“样本按列”的约定
X = X.T        # (2, 4)
Y = Y.T        # (1, 4)

n_samples = X.shape[1]   # 4



# 网络

net = Network([
    Linear(2, 8),
    ReLU(),
    Linear(8, 8),
    ReLU(),
    Linear(8, 1),
    Sigmoid(),
])

loss_fn = MSELoss()
lr = 0.5



#  训练

for epoch in range(10000):
    # ---- 前向 ----
    Y_hat = net.forward(X)
    loss = loss_fn.forward(Y_hat, Y)

    # ---- 反向 ----
    dZ = loss_fn.backward()
    net.backward(dZ)

    # ---- 更新 ----
    net.update(lr, n_samples)

    if epoch % 1000 == 0:
        print(f"Epoch {epoch:5d}, Loss: {loss:.6f}")



# 预测

print("\n预测对比：")
print(f"{'x1':>4} {'x2':>4} {'真实y':>8} {'预测y':>10}")

Y_hat = net.forward(X)
for i in range(n_samples):
    x1, x2 = X[0, i], X[1, i]
    real = Y[0, i]
    pred = Y_hat[0, i]
    print(f"{x1:>4} {x2:>4} {real:>8} {pred:>10.4f}")