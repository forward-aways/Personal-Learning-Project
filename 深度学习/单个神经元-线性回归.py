# 训练数据
xs = [1, 2, 3, 4, 5]
ys = [5, 8, 11, 14, 17]

# 参数，最开始随意给
w = 0.0
b = 0.0

# 学习率
lr = 0.01

for epoch in range(1000):
    dw = 0.0
    db = 0.0
    total_loss = 0.0

    for x, y in zip(xs, ys):
        # 1.前向传播: 算预测值
        pred = w * x + b

        # 2.算损失: 预测和真实差多少
        loss = (pred - y) ** 2
        total_loss += loss

        # 3.反向传播: 算梯度，手推出来的
        # 损失对w的导数 = 2 * (pred - y) * x
        # 损失对b的导数 = 2 * (pred - y)
        dw += 2 * (pred - y) * x
        db += 2 * (pred - y)

    # 4.更新参数: 往梯度反方向走一小步
    w -= lr * dw / len(xs)
    b -= lr * db / len(xs)

    if epoch % 100 == 0:
        print(f"第{epoch:4d}轮, 总损失: {total_loss:.4f}, w: {w:.4f}, b: {b:.4f}")

print(f"\n最终学到的: w={w:.4f}, b={b:.4f} ")
print(f"真实规律: w=3.000, b=2.000")