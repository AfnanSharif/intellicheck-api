my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Access the first element
print(my_list[-1])  # Access the last element

# Slicing lists
print(my_list[1:4])  # Get elements from index 1 to 3 (exclusive)

# Adding elements
my_list.append(6)  # Add 6 to the end
my_list.insert(2, 10)  # Insert 10 at index 2

# Removing elements
my_list.remove(3)  # Remove the first occurrence of 3
del my_list[1]  # Delete the element at index 1

print(my_list)