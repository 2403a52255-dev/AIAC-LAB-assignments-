import argparse
import random
import time
from typing import List, Callable

#!/usr/bin/env python3
"""
Task1.py

Compare Bubble Sort and Insertion Sort execution times using Python's time module.

Usage:
    python Task1.py            # runs with defaults (size=1000, runs=5)
    python Task1.py --size 2000 --runs 3
"""



def bubble_sort(a: List[int]) -> None:
    """In-place optimized bubble sort."""
    n = len(a)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break


def insertion_sort(a: List[int]) -> None:
    """In-place insertion sort."""
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # Move elements of a[0..i-1], that are greater than key, one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def measure_time(sort_fn: Callable[[List[int]], None], data: List[int]) -> float:
    """Measure execution time (seconds) of sort_fn on a copy of data."""
    arr = data.copy()
    t0 = time.perf_counter()
    sort_fn(arr) 
    t1 = time.perf_counter()
    # sanity check: ensure sorted
    if arr != sorted(data):
        raise RuntimeError(f"{sort_fn.__name__} did not sort correctly")
    return t1 - t0


def main():
    parser = argparse.ArgumentParser(description="Compare Bubble Sort and Insertion Sort timings.")
    parser.add_argument("--size", type=int, default=1000, help="Size of the random list (default: 1000)")
    parser.add_argument("--runs", type=int, default=5, help="Number of runs to average (default: 5)")
    args = parser.parse_args()

    size = args.size
    runs = args.runs

    bubble_times = []
    insertion_times = []

    for r in range(runs):
        # generate random list (with possible duplicate values)
        data = [random.randint(0, size * 10) for _ in range(size)]

        bt = measure_time(bubble_sort, data)
        it = measure_time(insertion_sort, data)

        bubble_times.append(bt)
        insertion_times.append(it)

        print(f"Run {r+1}/{runs}: bubble={bt:.6f}s, insertion={it:.6f}s")

    avg_bubble = sum(bubble_times) / runs
    avg_insertion = sum(insertion_times) / runs

    print("\nAverages:")
    print(f"Bubble Sort   : {avg_bubble:.6f} seconds (avg over {runs} runs)")
    print(f"Insertion Sort: {avg_insertion:.6f} seconds (avg over {runs} runs)")

    faster = "bubble sort" if avg_bubble < avg_insertion else "insertion sort"
    print(f"\nConclusion: On this data and environment, {faster} is faster.")


if __name__ == "__main__":
    main()