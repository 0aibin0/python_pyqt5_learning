import tkinter as tk
from tkinter import messagebox


def show_welcome_message():
    user_name = entry.get()
    welcome_message = f"欢迎你，{user_name}!"
    messagebox.showinfo("欢迎", welcome_message)


# 创建主窗口
root = tk.Tk()
root.title("欢迎程序")

# 添加组件
label = tk.Label(root, text="请输入你的名字:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="欢迎", command=show_welcome_message)
button.pack(pady=10)

# 进入主循环
root.mainloop()
