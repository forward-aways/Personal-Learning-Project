import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# 训练数据
xs = [-0.5, -0.3, -0.1, 0.1, 0.3, 0.5]
ys = [sigmoid(3 * x + 2) for x in xs]

# 参数，最开始随意给
w = 0.0
b = 0.0

# 学习率
lr = 2.0

for epoch in range(1000):
    dw = 0.0
    db = 0.0
    total_loss = 0.0

    for x, y in zip(xs, ys):
        # 1.前向传播: 算预测值
        z = w * x + b
        pred = sigmoid(z)

        # 2.算损失: 预测和真实差多少
        loss = (pred - y) ** 2
        total_loss += loss

        # 3.反向传播: 算梯度，手推出来的
        # 损失对w的导数 = 2 * (pred - y) * x
        # 损失对b的导数 = 2 * (pred - y)
        common = 2 * (pred - y) * pred * (1 - pred)
        dw += common * x
        db += common

    # 4.更新参数: 往梯度反方向走一小步
    w -= lr * dw / len(xs)
    b -= lr * db / len(xs)

    if epoch % 100 == 0:
        print(f"第{epoch:4d}轮, 总损失: {total_loss:.4f}, w: {w:.4f}, b: {b:.4f}")

print(f"\n最终学到的: w={w:.4f}, b={b:.4f} ")
print(f"真实规律: w=3.000, b=2.000")