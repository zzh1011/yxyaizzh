import tkinter as tk
import random
import threading
import time


def create_float_text():
    # 1. 初始化窗口
    window = tk.Tk()
    window.attributes('-alpha', 0.8)  # 窗口初始透明度（0.8为80%透明）
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 200
    window_height = 50
    # 随机定位窗口
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    window.title('漂浮字幕')
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    # 2. 定义字幕内容列表（可自定义添加）
    texts = [
        '愿杨欣怡天天开心', '祝杨欣怡金榜题名', '祝杨欣怡生活愉快', '愿杨欣怡梦想成真', '愿杨欣怡烦恼全清',
        '祝杨欣怡财源滚滚', '愿杨欣怡每天顺顺利利', '杨欣怡保持开心哦~', '天冷加衣', '早点休息',
        '别熬夜', '期待和你见面', '愿欣怡，平安喜乐', '愿欣怡，万事顺遂', '愿欣怡，心想事成'
    ]
    text = random.choice(texts)  # 随机选一条字幕

    # 3. 定义背景颜色列表（可自定义添加）
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender', 'lightyellow',
        'plum', 'coral', 'bisque', 'aquamarine', 'mistyrose'
    ]
    bg = random.choice(bg_colors)  # 随机选一个背景色

    # 4. 创建文字标签并设置样式
    tk.Label(
        window,
        text=text,
        bg=bg,
        font=('微软雅黑', 16, 'bold'),  # 字体、大小、加粗
        width=20,
        height=2
    ).pack()

    # 5. 窗口置顶（确保在所有窗口上层显示）
    window.attributes('-topmost', True)

    # 6. 定义“逐渐消散”函数（核心动画逻辑）
    def fade_out():
        alpha = window.attributes('-alpha')
        if alpha > 0:
            window.attributes('-alpha', alpha - 0.05)  # 每次降低5%透明度
            window.after(200, fade_out)  # 200毫秒后再次执行，控制消散速度
        else:
            window.destroy()  # 透明度为0时销毁窗口

    # 7. 启动消散倒计时（8000毫秒=8秒后开始消散，可修改）
    window.after(8000, fade_out)
    window.mainloop()  # 启动Tkinter事件循环


def qqq():
    # 8. 多线程生成满屏效果
    threads = []
    for i in range(100):  # 生成100个漂浮字幕（可调整数量）
        t = threading.Thread(target=create_float_text)
        threads.append(t)
        time.sleep(0.01)  # 每0.01秒启动一个线程，避免卡顿
        t.start()


qqq()