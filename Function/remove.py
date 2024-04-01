def remove_item(lst, item):
    """
    Removes the specified item from the given list.
    
    Args:
    lst (list): The list from which the item is to be removed.
    item: The item to be removed from the list.
    
    Returns:
    list: The updated list after removing the item.
    """
    try:
        lst.remove(item)
        return lst
    except ValueError:
        print(f"{item} not found in the list.")
        return lst

# Example usage:
my_list = [1, 2, 3, 4, 5]
item_to_remove = 3
updated_list = remove_item(my_list, item_to_remove)
print("Updated list:", updated_list)
