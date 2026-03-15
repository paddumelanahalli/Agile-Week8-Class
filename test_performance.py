#test_performance.py
import pytest
import time
from processor_example import process_data1


def test_execution_time():
    start_time = time.time()

    # We ask the processor to handle 100,000 items
    process_data1(100000)

    end_time = time.time()
    duration = end_time - start_time

    print(f"\nExecution time: {duration:.4f}s")

    # The test FAILs if it takes longer than 0.1 seconds
    assert duration < 0.1, f"Performance too slow! Took {duration:.4f}s"


# src/processor_example.py

def process_data1(n):
    """
    Optimized refactor using list comprehension.
    This is significantly faster than a standard for-loop in Python.
    """
    return [i * 2 for i in range(n)]

