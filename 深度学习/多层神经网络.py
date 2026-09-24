import math
import random

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def leaky_relu(z, alpha=0.25):
    return z if z > 0 else alpha * z

def leaky_relu_derivative(z, alpha=0.25 ):
    return 1 if z > 0 else alpha

xs = [-2, -1, 0, 1, 2, 3]
ys = [0.9, 0.3, 0.05, 0.3, 0.9, 0.98]   # U 形

# 3 个隐藏神经元
H = 3

random.seed(42)   # 固定随机种子，结果可复现

w1 = [random.uniform(-1, 1) for _ in range(H)]
b1 = [random.uniform(-1, 1) for _ in range(H)]
w2 = [random.uniform(-1, 1) for _ in range(H)]
b2 = random.uniform(-1, 1)

lr = 0.5

for epoch in range(5000):
    # 梯度累加器（注意是列表）
    dw1 = [0.0] * H
    db1 = [0.0] * H
    dw2 = [0.0] * H
    db2 = 0.0
    total_loss = 0.0

    for x, y in zip(xs, ys):
        # 前向传播
        z1 = [0.0] * H
        h = [0.0] * H
        for i in range(H):
            z1[i] = w1[i] * x + b1[i]
            h[i] = leaky_relu(z1[i])

        z2 = 0.0
        for i in range(H):
            z2 += w2[i] * h[i]
        z2 += b2
        y_hat = sigmoid(z2)

        loss = (y_hat - y) ** 2
        total_loss = loss

        # 反向传播
        delta2 = 2 *  (y_hat - y) * y_hat * (1 - y_hat)

        for i in range(H):
            # 输出层
            dw2[i] += delta2 * h[i]

            # 隐藏层
            delta1 = delta2 * w2[i] * leaky_relu_derivative(z1[i])
            dw1[i] += delta1 * x
            db1[i] += delta1

        db2 += delta2

    #  更新
    n = len(xs)

    for i in range(H):
        w1[i] -= lr * dw1[i] / n
        b1[i] -= lr * db1[i] / n
        w2[i] -= lr * dw2[i] / n
    b2 -= lr * db2 / n

    if epoch % 500 == 0:
        print(f"第{epoch:4d}轮, 总损失: {total_loss:.6f}")
        print(f"训练后参数: w1={w1}, b1={b1}, w2={w2}, b2={b2}")

    # 预测输出
print("\n预测对比：")
print(f"{'x':>5} {'真实y':>10} {'预测y':>10} {'误差':>10}")
for x, y in zip(xs, ys):
    h = [leaky_relu(w1[i] * x + b1[i]) for i in range(H)]
    z2 = sum(w2[i] * h[i] for i in range(H)) + b2
    y_hat = sigmoid(z2)
    print(f"{x:>5} {y:>10.4f} {y_hat:>10.4f} {abs(y_hat - y):>10.4f}")