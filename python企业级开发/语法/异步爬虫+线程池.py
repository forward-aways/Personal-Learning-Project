import asyncio
from concurrent.futures import ThreadPoolExecutor


def legacy_fetch(url: str) -> str:
    import time
    time.sleep(0.5)
    return f"<html> {url} </html>"


async def crawl(url: str, pool: ThreadPoolExecutor, sem: asyncio.Semaphore):
    async with sem:
        # 拿到当前事件循环
        loop = asyncio.get_running_loop()
        try:
            # 使用 asyncio.wait_for 设置超时
            html = await asyncio.wait_for(
                # 使用当前事件循环的 run_in_executor 方法，异步执行 legacy_fetch 函数
                loop.run_in_executor(pool, legacy_fetch, url),
                # 设置超时时间为 3 秒
                timeout=3,
            )

            return url, len(html)
        except asyncio.TimeoutError:
            return url, -1


async def main():
    urls = [f"https://example.com/{i}" for i in range(20)]
    # 创建一个信号量，限制并发数为 10
    sem = asyncio.Semaphore(10)

    # 创建一个线程池，最大线程数为 10
    with ThreadPoolExecutor(max_workers=10) as pool:
        # 使用 asyncio.gather 并发执行 crawl 函数，传入 urls 列表中的每个 url
        # 并发数为 10，即同时执行 10 个 crawl 函数
        results = await asyncio.gather(*(crawl(u, pool, sem) for u in urls)) # *是解包操作符

    for url, size in results:
        print(url, size)


if __name__ == '__main__':
    asyncio.run(main())