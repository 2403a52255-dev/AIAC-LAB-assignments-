def sort_list(data):
    def get_sort_key(item):
        if isinstance(item, int):
            return (0, item)  # Numbers first, sorted by value
        else:
            return (1, str(item))  # Strings second, sorted alphabetically
    
    return sorted(data, key=get_sort_key)

items = [3, "apple", 1, "banana", 2]
print(sort_list(items))