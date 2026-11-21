
# CA3: Process vs Thread Creation

## 1. Introduction

An operating system manages programs and their execution. Two important concepts in this process are processes and threads.

A process is an independent program in execution with its own memory space. A thread is a unit of execution within a process. Threads belonging to the same process share memory and resources.

This project compares process-based and thread-based execution using Python.

## 2. Objectives

- Understand process and thread creation.
- Implement the same CPU-intensive task using threads and processes.
- Measure and compare execution time.
- Verify that both approaches produce the same results.
- Analyse the performance differences.

## 3. Tools and Technologies

- Operating System: Ubuntu Linux
- Programming Language: Python 3.12.3
- Libraries: time, concurrent.futures
- Editor: Nano

## 4. Implementation

The program performs a mathematical calculation using two approaches:

1. ThreadPoolExecutor: Runs the calculation using multiple threads.
2. ProcessPoolExecutor: Runs the calculation using multiple processes.

Both approaches use two workers and perform the same calculation. Python's time.perf_counter() function measures execution time.

## 5. Experimental Results

### Experiment 1: Repeated Benchmark

The experiment was repeated five times using 2,000,000 iterations per worker.

| Run | Threads (s) | Processes (s) |
|---|---:|---:|
| 1 | 0.2775 | 0.1301 |
| 2 | 0.3028 | 0.1319 |
| 3 | 0.2717 | 0.1420 |
| 4 | 0.2478 | 0.1376 |
| 5 | 0.2454 | 0.1530 |
| Average | 0.26904 | 0.13892 |

### Experiment 2: Different Workloads

Two workers were used for each workload.

| Workload per worker | Threads (s) | Processes (s) |
|---:|---:|---:|
| 500,000 | 0.0576 | 0.0365 |
| 2,000,000 | 0.2398 | 0.1181 |
| 5,000,000 | 0.5971 | 0.3259 |

Both methods produced identical calculation results in every test.

## 6. Analysis

The results show that multiprocessing was faster than multithreading for the tested CPU-intensive calculations.

Python's Global Interpreter Lock (GIL) limits parallel execution of Python bytecode by threads in standard CPython. Separate processes can execute independently and may use multiple CPU cores.

As the workload increased, execution time also increased. Multiprocessing remained faster in all three workload tests.

However, process creation and communication introduce overhead. The results depend on the system, workload and execution conditions, and should not be treated as universal.

## 7. Conclusion

The experiment demonstrated the practical differences between processes and threads.

For this particular CPU-intensive task, multiprocessing achieved a lower average execution time than multithreading.

Threads are useful for tasks involving waiting, such as input/output operations, while processes can be more suitable for CPU-intensive work that benefits from parallel execution.

## 8. Limitations

- Only one computer and Python version were used.
- The experiment used two workers.
- Only one workload size was used in the repeated benchmark.
- Execution times may vary between runs.
- The measurements include worker-pool startup overhead and do not isolate creation time alone.

## 9. How to Run

Make sure Python 3 is installed.

Run the following command from the project directory:

    python3 thread_vs_process.py
