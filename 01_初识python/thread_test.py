"""
在这个示例中，我们定义了一个 MyThread 类，它继承自 threading.Thread 类，并重写了 run 方法。
在 run 方法中，我们使用了一个 while 循环来持续执行线程的任务，同时检查了一个 _stop_event 标志，
以决定是否停止线程。stop 方法用于设置 _stop_event 标志，以通知线程停止执行。
"""

import threading
import time


class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            print("Thread is running...")
            time.sleep(1)

    def stop(self):
        print("Stopping thread...")
        self._stop_event.set()


# 创建线程实例
my_thread = MyThread()
# 启动线程
my_thread.start()

# 等待一段时间
time.sleep(5)

# 停止线程
my_thread.stop()
# 等待线程结束
my_thread.join()

print("Main thread ends")
