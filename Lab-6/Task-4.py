def sum_first_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# --- Check Output ---
print("Sum of first 10 numbers (for loop):", sum_first_n_for(10))
