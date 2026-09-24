import torch
import torch.nn as nn

torch.manual_seed(123)

# 数据
# 形状：（样本数，特征数）pytorch的约定
xs = torch.tensor([[-2.], [-1.], [0.], [1.], [2.], [3.]])   # (6, 1)
ys = torch.tensor([[0.9], [0.3], [0.05], [0.3], [0.9], [0.98]])  # (6, 1)

# 测试用 2 个点（训练时没见过）
xs_test = torch.tensor([[0.], [3.]])
ys_test = torch.tensor([[0.05], [0.98]])

# 定义网络
model = nn.Sequential(
    nn.Linear(1, 16), # 输入1维，输出16维
    nn.LeakyReLU(0.01),
    nn.Linear(16, 16), # 输入16维，输出16维
    nn.LeakyReLU(0.01),       # 隐藏层激活函数，负斜率为0.25
    nn.Linear(16, 16),  # 输入16维，输出16维
    nn.LeakyReLU(0.01),       # 隐藏层激活函数，负斜率为0.25
    nn.Linear(16, 1)  # 输入8维，输出1维

)

# 定义损失函数和优化器
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
# 学习率调度器
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1000, gamma=0.5)  # 学习率每1000轮下降0.1

# 训练
for epoch in range(5000):
    # 前向传播
    y_hat = model(xs)
    loss = loss_fn(y_hat, ys)

    # 反向传播
    optimizer.zero_grad() # 清空上一轮的梯度
    loss.backward() # 自动算梯度
    optimizer.step() # 更新参数
    scheduler.step()

    if epoch % 500 == 0:
        print(f"Epoch {epoch:5d}, Loss: {loss:.6f}")

with torch.no_grad():                    # 预测时不算梯度
    y_hat = model(xs_test)

print("\n预测对比：")
print(f"{'x':>5} {'真实y':>10} {'预测y':>10} {'误差':>10}")
for i in range(len(xs_test)):
    x = xs_test[i].item()
    real = ys_test[i].item()
    pred = y_hat[i].item()
    print(f"{x:>5.0f} {real:>10.4f} {pred:>10.4f} {abs(pred - real):>10.4f}")

