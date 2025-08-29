def compute_ratios(values):
    return [(i, j, values[i] / (values[j] - values[i])) 
            for i in range(1, len(values)) 
            for j in range(i, len(values)) 
            if values[j] - values[i] != 0]

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))