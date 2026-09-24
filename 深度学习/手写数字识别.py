# draw_digit.py
import tkinter as tk
from PIL import Image, ImageDraw
import torch
import torch.nn as nn
import numpy as np

# ============================================================
# 1. 模型结构（必须和训练时一致）
# ============================================================
def make_model():
    return nn.Sequential(
        nn.Conv2d(1, 32, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),
        nn.Conv2d(32, 64, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2, stride=2),
        nn.Flatten(),
        nn.Linear(64 * 7 * 7, 128),
        nn.ReLU(),
        nn.Linear(128, 10),
    )

# 加载模型
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = make_model().to(device)
model.load_state_dict(torch.load("mnist_cnn.pth", map_location=device))
model.eval()
print("模型加载完成")


# ============================================================
# 2. 图片预处理（模拟 MNIST 格式）
# ============================================================
def preprocess(image):
    """
    把画板图片转成 MNIST 风格：
    1. 裁剪到数字边界
    2. 缩放到 20x20
    3. 居中放到 28x28 黑底
    """
    bbox = image.getbbox()
    if bbox is None:
        return None

    cropped = image.crop(bbox)
    w, h = cropped.size

    scale = 20 / max(w, h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    resized = cropped.resize((new_w, new_h), Image.LANCZOS)

    final = Image.new("L", (28, 28), 0)
    offset_x = (28 - new_w) // 2
    offset_y = (28 - new_h) // 2
    final.paste(resized, (offset_x, offset_y))

    return final


# ============================================================
# 3. GUI
# ============================================================
CANVAS_SIZE = 280
BRUSH_SIZE = 16

root = tk.Tk()
root.title("手写数字识别")
root.resizable(False, False)

# 画板
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE,
                   bg="black", cursor="crosshair")
canvas.pack(padx=10, pady=10)

# 用 PIL 图片记录画的内容（黑底白字）
image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), 0)
draw = ImageDraw.Draw(image)

last_x, last_y = None, None


def on_press(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y


def on_drag(event):
    global last_x, last_y
    if last_x is not None:
        # tkinter Canvas 显示
        canvas.create_line(last_x, last_y, event.x, event.y,
                           fill="white", width=BRUSH_SIZE,
                           capstyle=tk.ROUND, smooth=True)
        # PIL 图片同步记录
        draw.line([last_x, last_y, event.x, event.y],
                  fill=255, width=BRUSH_SIZE, joint="curve")
        draw.ellipse([event.x - BRUSH_SIZE//2, event.y - BRUSH_SIZE//2,
                      event.x + BRUSH_SIZE//2, event.y + BRUSH_SIZE//2],
                     fill=255)
    last_x, last_y = event.x, event.y


def on_release(event):
    global last_x, last_y
    last_x, last_y = None, None


canvas.bind("<Button-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)


# ---- 按钮区 ----
def predict():
    processed = preprocess(image)
    if processed is None:
        result_label.config(text="请先写一个数字")
        return

    # 转成 tensor：(1, 1, 28, 28)
    arr = np.array(processed, dtype=np.float32) / 255.0
    tensor = torch.tensor(arr).unsqueeze(0).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(tensor)
        probs = torch.softmax(output, dim=1)[0]
        pred = output.argmax(dim=1).item()
        confidence = probs[pred].item()

    result_label.config(text=f"预测: {pred}    置信度: {confidence:.2%}")


def clear():
    global image, draw
    canvas.delete("all")
    image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), 0)
    draw = ImageDraw.Draw(image)
    result_label.config(text="请写一个数字")


# 按钮
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="识别", command=predict,
          font=("Arial", 14), width=8).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="清除", command=clear,
          font=("Arial", 14), width=8).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="请写一个数字",
                        font=("Arial", 16), fg="blue")
result_label.pack(pady=5)

root.mainloop()