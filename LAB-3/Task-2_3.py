def sort_strings_from_input():
    user_input = input("Enter strings separated by spaces: ")
    str_list = user_input.strip().split()
    sorted_list = sorted(str_list)
    print(f"Sorted strings: {sorted_list}")

sort_strings_from_input()
