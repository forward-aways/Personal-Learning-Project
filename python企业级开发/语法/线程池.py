import time
import concurrent.futures
from turtledemo.penrose import start


def cpu_bound_task(task_id, duration=2):
    print(f"任务 {task_id} 开始工作，耗时 {duration} 秒")
    time.sleep(duration)
    print(f"任务 {task_id} 完成")
    return f"任务 {task_id} 的结果"

def main_sync():
    """同步方式执行任务"""
    print("开始同步方式执行任务")
    start = time.time()
    results = []
    for i in range(5):
        result = cpu_bound_task(i)
        results.append(result)

    print(f"同步方式执行任务耗时 {time.time() - start:.2f} 秒")
    print(f"同步方式执行任务结果 {results}")


def main_threadpool():
    """线程池版"""
    print("线程池开始执行")
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # submit把任务提交给线程池，返回一个future对象
        futures = [executor.submit(cpu_bound_task, i, 2) for i in range(5)]
        # as_completed返回一个迭代器，包含已完成的future对象
        results = [f.result() for f in concurrent.futures.as_completed(futures)]


    print(f"结果 {results}")
    print(f"总耗时 {time.time() - start:.2f} 秒")

if __name__ == '__main__':
    main_sync()
    main_threadpool()