import math
import random

random.seed(42)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# XOR 数据
xs = [[0, 0], [0, 1], [1, 0], [1, 1]]
ys = [0, 1, 1, 0]

# 隐藏层 2 个神经元，每个接收 2 个输入
H = 2
w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(H)]  # 2x2
b1 = [random.uniform(-1, 1) for _ in range(H)]                       # 2
w2 = [random.uniform(-1, 1) for _ in range(H)]                       # 2
b2 = random.uniform(-1, 1)                                            # 1

lr = 0.5

for epoch in range(10000):
    dw1 = [[0.0] * 2 for _ in range(H)]
    db1 = [0.0] * H
    dw2 = [0.0] * H
    db2 = 0.0
    total_loss = 0.0

    for x, y in zip(xs, ys):
        x1, x2 = x

        # ---- 前向 ----
        z1 = [0.0] * H
        h = [0.0] * H
        for i in range(H):
            z1[i] = w1[i][0] * x1 + w1[i][1] * x2 + b1[i]
            h[i] = sigmoid(z1[i])

        z2 = sum(w2[i] * h[i] for i in range(H)) + b2
        y_hat = sigmoid(z2)

        loss = (y_hat - y) ** 2
        total_loss += loss

        # ---- 反向 ----
        delta2 = 2 * (y_hat - y) * y_hat * (1 - y_hat)

        for i in range(H):
            dw2[i] += delta2 * h[i]
            delta1 = delta2 * w2[i] * h[i] * (1 - h[i])
            dw1[i][0] += delta1 * x1
            dw1[i][1] += delta1 * x2
            db1[i] += delta1

        db2 += delta2

    n = len(xs)
    for i in range(H):
        for j in range(2):
            w1[i][j] -= lr * dw1[i][j] / n
        b1[i] -= lr * db1[i] / n
        w2[i] -= lr * dw2[i] / n
    b2 -= lr * db2 / n

    if epoch % 1000 == 0:
        print(f"第{epoch:5d}轮, 总损失: {total_loss:.6f}")

print(f"\n最终参数:")
print(f"w1 = {w1}")
print(f"b1 = {b1}")
print(f"w2 = {w2}")
print(f"b2 = {b2:.4f}")

print("\n预测对比：")
print(f"{'x1':>4} {'x2':>4} {'真实y':>8} {'预测y':>10} {'误差':>10}")
for x, y in zip(xs, ys):
    x1, x2 = x
    h = [sigmoid(w1[i][0] * x1 + w1[i][1] * x2 + b1[i]) for i in range(H)]
    z2 = sum(w2[i] * h[i] for i in range(H)) + b2
    y_hat = sigmoid(z2)
    print(f"{x1:>4} {x2:>4} {y:>8} {y_hat:>10.4f} {abs(y_hat - y):>10.4f}")