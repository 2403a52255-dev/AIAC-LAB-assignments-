def sort_list_from_input():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        lst = [int(x) for x in user_input.strip().split()]
        sorted_lst = sorted(lst)
        print(f"Sorted list: {sorted_lst}")
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")

sort_list_from_input()
