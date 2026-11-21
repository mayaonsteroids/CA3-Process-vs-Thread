import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def calculate(number):
    total = 0
    for i in range(number):
        total += i * i
    return total


def run_test(executor_class, workers, number):
    start = time.perf_counter()

    with executor_class(max_workers=workers) as executor:
        results = list(executor.map(calculate, [number] * workers))

    end = time.perf_counter()
    return end - start, results


if __name__ == "__main__":
    workers = 2
    workloads = [500_000, 2_000_000, 5_000_000]

    print("PROCESS VS THREAD: WORKLOAD TEST")
    print("--------------------------------")

    for number in workloads:
        thread_time, thread_results = run_test(
            ThreadPoolExecutor, workers, number
        )

        process_time, process_results = run_test(
            ProcessPoolExecutor, workers, number
        )

        print(f"\nWorkload per worker: {number:,}")
        print(f"Threads: {thread_time:.4f} seconds")
        print(f"Processes: {process_time:.4f} seconds")
        print("Same results:", thread_results == process_results)
