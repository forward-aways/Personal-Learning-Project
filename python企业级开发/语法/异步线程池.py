import asyncio
import time


# 模拟一个同步阻塞库（比如 openpyxl.load_workbook 或 pandas.read_excel）
def sync_blocking_task(name, seconds):
    print(f"  [阻塞任务 {name}] 开始占用 CPU 并阻塞 {seconds} 秒...")
    time.sleep(seconds)  # 模拟解析大文件时的 CPU 计算
    print(f"  [阻塞任务 {name}] 完成！")
    return f"{name} 的数据"


# 一个纯粹的异步 IO 协程（比如定时心跳，或者处理其他网络请求）
async def heartbeat():
    for i in range(6):  # 总共运行 6 次
        await asyncio.sleep(0.5)  # 每 0.5 秒让出 CPU
        print(f"  [心跳] 当前时间: {time.strftime('%X')} (主循环没有被卡死！)")


async def main():
    print(">>> 启动异步主程序")
    start = time.time()

    # 1. 启动心跳协程（不阻塞）
    asyncio.create_task(heartbeat())

    # 2. 使用 asyncio.to_thread 把 3 个同步阻塞任务扔进线程池
    #    这 3 个任务会由操作系统的线程并行执行（绕过 GIL 影响，或至少不阻塞主循环）
    tasks = [
        asyncio.to_thread(sync_blocking_task, "Excel_导入", 2),
        asyncio.to_thread(sync_blocking_task, "PDF_生成", 3),
        asyncio.to_thread(sync_blocking_task, "图片_压缩", 1),
    ]

    # 3. 并发等待它们全部完成（总耗时约 3 秒，而不是 2+3+1=6 秒）
    results = await asyncio.gather(*tasks)

    print(f">>> 所有结果: {results}")
    print(f">>> 总墙钟耗时: {time.time() - start:.2f} 秒")


if __name__ == "__main__":
    asyncio.run(main())