import numpy as np
import time


SIZE = 1_000_000

# Python list
python_data = list(range(SIZE))

# NumPy array
numpy_data = np.arange(SIZE)

# -------- Python Loop --------
start = time.perf_counter()

result_loop = []
for x in python_data:
    result_loop.append(x * 2)

loop_time = time.perf_counter() - start

# -------- NumPy Vectorized --------
start = time.perf_counter()

result_numpy = numpy_data * 2

numpy_time = time.perf_counter() - start


print(f"Loop time:   {loop_time:.6f} seconds")
print(f"NumPy time:  {numpy_time:.6f} seconds")
print(f"Speedup:     {loop_time / numpy_time:.2f}x faster")
