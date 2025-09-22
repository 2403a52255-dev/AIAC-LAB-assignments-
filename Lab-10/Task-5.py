
import time

start_time = time.time()
# Using list comprehension for faster execution
squares = [n**2 for n in range(1, 1000000)]
print(len(squares))
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")

