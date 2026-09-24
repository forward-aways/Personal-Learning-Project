import torch
import torch.nn as nn
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LRScheduler



# 创建优化器和学习率调度器
def make_optimizer_and_scheduler(
        model,
        optimizer_name='Adam',
        lr=0.01,
        scheduler_name='StepLR',
        step_size=1000,
        gamma=0.5
) -> tuple[Optimizer, LRScheduler]:
    """
    创建统一的优化器和学习率调度器

    Args:
        model (nn.Module):          模型
        optimizer_name (str):       优化器名称，默认'Adam'
        lr (float):                 学习率，默认0.01
        scheduler_name (str):       学习率调度器名称，默认'StepLR'
        step_size (int):            学习率调度器的步长，默认1000
        gamma (float):              学习率调度器的衰减率，默认0.5
    Returns:
        (optimizer, scheduler)
    """

    # 优化器
    if optimizer_name == "Adam":
        optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    elif optimizer_name == "SGD":
        optimizer = torch.optim.SGD(model.parameters(), lr=lr)
    elif optimizer_name == "AdamW":
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    else:
        raise ValueError(f"未知的优化器名称: {optimizer_name}")


    # 学习率调度器
    if scheduler_name == "StepLR":
        scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=step_size, gamma=gamma)
    elif scheduler_name == "CosineAnnealingLR":
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=step_size, eta_min=0)
    else:
        raise ValueError(f"未知的学习率调度器名称: {scheduler_name}")

    # 返回优化器和学习率调度器
    return optimizer, scheduler



# 训练函数
def train(
        model,
        xs,
        ys,
        loss_fn,
        optimizer,
        scheduler,
        epochs=1000,
        print_every=100
):
    """
    训练循环

    Args:
        model (nn.Module):                                  模型
        xs (torch.Tensor):                                  输入数据
        ys (torch.Tensor):                                  目标数据
        loss_fn (nn.Module):                                损失函数
        optimizer (torch.optim.Optimizer):                  优化器
        scheduler (torch.optim.lr_scheduler._LRScheduler):  学习率调度器
        epochs (int):                                       训练轮数，默认1000
        print_every (int):                                  每多少轮打印一次，默认100

    Returns:
        训练好的模型
    """
    model.train()

    for epoch in range(epochs):
        # 前向传播
        y_hat = model(xs)
        loss = loss_fn(y_hat, ys)

        # 反向传播+更新（优化）
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # 更新学习率
        if scheduler is not None:
            scheduler.step()

        # 打印
        if epoch % print_every == 0:
            current_lr = optimizer.param_groups[0]['lr']
            print(f"Epoch {epoch:5d}, Loss: {loss.item():.6f}, learning_rate: {current_lr:.6f}")

    return model



# 定义数据
torch.manual_seed(42)

xs = torch.tensor([[-2.], [-1.], [0.], [1.], [2.], [3.]])
ys = torch.tensor([[0.9], [0.3], [0.05], [0.3], [0.9], [0.98]])


# 主流程

if __name__ == '__main__':
    # 定义模型
    model = nn.Sequential(
        nn.Linear(1, 16),
        nn.LeakyReLU(0.01),
        nn.Linear(16, 16),
        nn.LeakyReLU(0.01),
        nn.Linear(16, 1),
    )

    loss_fn = nn.MSELoss()
    optimizer, scheduler = make_optimizer_and_scheduler(
        model=model,
        optimizer_name='Adam',
        lr=0.01,
        scheduler_name='StepLR',
        step_size=1000,
        gamma=0.5
    )

    model = train(
        model=model,
        xs=xs,
        ys=ys,
        loss_fn=loss_fn,
        optimizer=optimizer,
        scheduler=scheduler,
        epochs=1000,
        print_every=100
    )

    # 设置模型为评估模式
    model.eval()
    with torch.no_grad():
        y_hat = model(xs)

    print("\n预测对比")
    print(f"{'x':>5} {'真实y':>10} {'预测y':>10} {'误差':>10}")
    for i in range(len(xs)):
        x = xs[i].item()
        real = ys[i].item()
        pred = y_hat[i].item()
        print(f"{x:>5.0f} {real:>10.4f} {pred:>10.4f} {abs(pred - real):>10.4f}")

