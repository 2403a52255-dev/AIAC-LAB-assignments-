def bubble_sort(arr):
    """
    Implements the Bubble Sort algorithm.
    Args:
        arr: List of comparable elements to sort  
    Returns:
        List: Sorted array in ascending order
    """
    # Create a copy to avoid modifying the original array
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize - if no swapping occurs, array is sorted
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True   
        # If no two elements were swapped, then the array is sorted
        if not swapped:
            break
    return sorted_arr
def is_sorted(arr):
    """
    Check if an array is sorted in ascending order.
    
    Args:
        arr: List to check
        
    Returns:
        bool: True if sorted, False otherwise
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
# Two input lists
list1 = [64, 34, 25, 12, 22, 11, 90]
list2 = [5, 2, 8, 1, 9, 3]
print("Bubble Sort Results")
print("=" * 30)
# Sort first list
print(f"\nList 1:")
print(f"Original:  {list1}")
sorted_list1 = bubble_sort(list1)
print(f"Sorted:    {sorted_list1}")
print(f"Is Sorted: {is_sorted(sorted_list1)}")
# Sort second list
print(f"\nList 2:")
print(f"Original:  {list2}")
sorted_list2 = bubble_sort(list2)
print(f"Sorted:    {sorted_list2}")
print(f"Is Sorted: {is_sorted(sorted_list2)}")
