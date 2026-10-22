import torch
import torch.nn as nn
from sympy import evaluate
from torch.optim import Optimizer
from torch.optim.lr_scheduler import LRScheduler
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


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


# 定义模型
def make_model() -> nn.Module:
    return nn.Sequential(
        nn.Flatten(),
        nn.Linear(784, 128),
        nn.ReLU(),
        nn.Dropout(0.2),                                # 添加dropout层,防止过拟合
        nn.Linear(128, 64),
        nn.ReLU(),
        nn.Linear(64, 10)
    )

# 评估函数
def evaluate(model, loader, loss_fn, device):
    """在给定数据集上评估，返回平均 loss 和准确率"""
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            loss = loss_fn(outputs, labels)

            total_loss += loss.item() * images.size(0)
            correct += (outputs.argmax(dim=1) == labels).sum().item()
            total += images.size(0)

    return total_loss / total, correct / total

# 训练一个epoch
def train(
        model,
        train_loader,
        test_loader,
        loss_fn,
        optimizer,
        scheduler,
        epochs=1000,
        device=None
):
    model.train()
    for epoch in range(epochs):
        total_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            # 前向传播
            outputs = model(images)
            loss = loss_fn(outputs, labels)

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item() * images.size(0)
            correct += (outputs.argmax(dim=1) == labels).sum().item()
            total += labels.size(0)

        train_loss = total_loss / total
        train_acc = correct / total

        # 评估
        test_loss, test_acc = evaluate(model, test_loader, loss_fn, device)

        # 调度
        if scheduler == "StepLR":
            scheduler.step()

        print(f"Epoch {epoch + 1}/{epochs} | "
              f"训练 loss={train_loss:.4f} acc={train_acc:.4f} | "
              f"测试 loss={test_loss:.4f} acc={test_acc:.4f}")



if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")

    transform = transforms.ToTensor()

    train_dataset = datasets.MNIST(
        root="./data", train=True, download=True, transform=transform
    )
    test_dataset = datasets.MNIST(
        root="./data", train=False, download=True, transform=transform
    )

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    print(f"训练集: {len(train_dataset)} 张")
    print(f"测试集: {len(test_dataset)} 张")

    model = make_model().to(device)

    loss_fn = nn.CrossEntropyLoss()
    optimizer, scheduler = make_optimizer_and_scheduler(
        model,
        optimizer_name="Adam",
        lr=0.001,
        scheduler_name="StepLR",
        step_size=3,
        gamma=0.5,
    )

    model = train(
        model=model,
        train_loader=train_loader,
        test_loader=test_loader,
        loss_fn=loss_fn,
        optimizer=optimizer,
        scheduler=scheduler,
        epochs=5,
        device=device,
    )