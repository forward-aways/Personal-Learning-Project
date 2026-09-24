// 1. 获取页面中的元素
const button = document.getElementById('myButton');
const messageBox = document.getElementById('messageBox');

// 2. 定义一个计数器（用来玩点花样）
let clickCount = 0;

// 3. 给按钮添加“点击事件监听器”
button.addEventListener('click', function() {
    // 每次点击，计数器加 1
    clickCount = clickCount + 1;

    // 根据点击次数，显示不同的消息
    if (clickCount === 1) {
        messageBox.textContent = ' 你第一次点击了我！';
        messageBox.style.color = '#27ae60';
    } else if (clickCount <= 5) {
        messageBox.textContent = ` 你已经点击了 ${clickCount} 次！`;
        messageBox.style.color = '#2c3e50';
    } else {
        messageBox.textContent = ` 天哪！你点了 ${clickCount} 次，手指不累吗？`;
        messageBox.style.color = '#e74c3c';
    }
});