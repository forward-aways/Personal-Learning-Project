import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# 训练数据：真实规律 y = sigmoid(2x)
xs = [-2, -1, 0, 1, 2, 3]
ys = [sigmoid(2 * x) for x in xs]

# 4 个参数，随便初始化
w1, b1 = 0.5, 0.0     # 隐藏层
w2, b2 = 0.5, 0.0     # 输出层

lr = 0.5

for epoch in range(5000):
    dw1 = db1 = dw2 = db2 = 0.0
    total_loss = 0.0

    for x, y in zip(xs, ys):
        # 前向传播
        z1 = w1 * x + b1
        h = sigmoid(z1)
        z2 = w2 * h + b2
        y_hat = sigmoid(z2)

        loss = (y_hat - y) ** 2
        total_loss += loss

        # 反向传播
        # 输出层
        delta2 = 2 * (y_hat - y) * y_hat * (1 - y_hat)
        dw2 += delta2 * h
        db2 += delta2

        # 隐藏层
        delta1 = delta2 * w2 * h * (1 - h)
        dw1 += delta1 * x
        db1 += delta1

    # 更新参数
    n = len(xs)
    w1 -= lr * dw1 / n
    b1 -= lr * db1 / n
    w2 -= lr * dw2 / n
    b2 -= lr * db2 / n

    if epoch % 500 == 0:
        print(f"第{epoch:4d}轮, 总损失: {total_loss:.4f}, w1: {w1:.4f}, b1: {b1:.4f}, w2: {w2:.4f}, b2: {b2:.4f}")

print(f"最终学到的: w1={w1:.4f}, b1={b1:.4f}, w2={w2:.4f}, b2={b2:.4f} ")

print("\n预测对比：")
print(f"{'x':>5} {'真实y':>10} {'预测y':>10} {'误差':>10}")
for x, y in zip(xs, ys):
    z1 = w1 * x + b1
    h = sigmoid(z1)
    z2 = w2 * h + b2
    y_hat = sigmoid(z2)
    print(f"{x:>5} {y:>10.4f} {y_hat:>10.4f} {abs(y_hat - y):>10.4f}")

