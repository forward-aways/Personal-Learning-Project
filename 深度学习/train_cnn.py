import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def make_model():
    return nn.Sequential(
        # ---- 卷积块 1 ----
        nn.Conv2d(1, 32, kernel_size=3, padding=1),   # (1,28,28) → (32,28,28)
        nn.ReLU(),
        nn.MaxPool2d(2),                              # (32,28,28) → (32,14,14)

        # ---- 卷积块 2 ----
        nn.Conv2d(32, 64, kernel_size=3, padding=1),  # (32,14,14) → (64,14,14)
        nn.ReLU(),
        nn.MaxPool2d(2),                              # (64,14,14) → (64,7,7)

        # ---- 全连接 ----
        nn.Flatten(),                                 # (64,7,7) → 3136
        nn.Linear(64 * 7 * 7, 128),
        nn.ReLU(),
        nn.Linear(128, 10),
    )

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用设备: {device}")

    # ---- 数据增强 ----
    train_transform = transforms.Compose([
        transforms.RandomAffine(degrees=15, translate=(0.1, 0.1), scale=(0.8, 1.2)),
        transforms.ToTensor(),
    ])
    test_transform = transforms.ToTensor()

    train_dataset = datasets.MNIST(root=r"D:\AI_Learning\test\深度学习\data", train=True,
                                    download=True, transform=train_transform)
    test_dataset = datasets.MNIST(root=r"D:\AI_Learning\test\深度学习\data", train=False,
                                   download=True, transform=test_transform)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    model = make_model().to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    epochs = 5
    for epoch in range(epochs):
        # ---- 训练 ----
        model.train()
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            outputs = model(images)
            loss = loss_fn(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # ---- 评估 ----
        model.eval()
        correct = total = 0
        with torch.no_grad():
            for images, labels in test_loader:
                images, labels = images.to(device), labels.to(device)
                preds = model(images).argmax(dim=1)
                correct += (preds == labels).sum().item()
                total += labels.size(0)
        print(f"Epoch {epoch+1}/{epochs}, 测试准确率: {correct/total:.4f}")

    torch.save(model.state_dict(), "mnist_cnn.pth")
    print("\n模型已保存到 mnist_cnn.pth")

if __name__ == "__main__":
    main()