def linear_search(arr, target):
    """
    Performs linear search to find the index of a target value in a list.    
    Args:
        arr (list): The list to search in
        target: The value to search for 
    Returns:
        int: The index of the target value if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
# Example usage and test cases
if __name__ == "__main__":
    # Test cases
    test_list = [10, 25, 3, 8, 15, 42, 7]
    print(f"List to search: {test_list}")
    print("-" * 40)
    # Test 1: Value exists in the list
    target1 = 15
    result1 = linear_search(test_list, target1)
    print(f"Searching for {target1}: Index = {result1}") 
    # Test 2: Value doesn't exist in the list
    target2 = 99
    result2 = linear_search(test_list, target2)
    print(f"Searching for {target2}: Index = {result2}") 
    # Test 3: Value at the beginning
    target3 = 10
    result3 = linear_search(test_list, target3)
    print(f"Searching for {target3}: Index = {result3}") 
    # Test 4: Value at the end
    target4 = 7
    result4 = linear_search(test_list, target4)
    print(f"Searching for {target4}: Index = {result4}")
    # Test 5: Empty list
    empty_list = []
    print(f"\nEmpty list to search: {empty_list}")
    result5 = linear_search(empty_list, 5)
    print(f"Searching for 5 in empty list: Index = {result5}")
