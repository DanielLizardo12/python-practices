#LISTS

my_list = [1, 2, 3]
print(len(my_list))

my_list = ["mix", 2, True, "asdf", [1, 2, 3]]
print(my_list)

my_list = ["a", "b", 'c', 'd', 'e']
print(my_list[:])
print(my_list[:3])

my_list[0] = "New Item"
print(my_list)

#my_list.append(['x', 'y', 'z']) # Add a list into your list "nest"
list_two = ['x', 'y', 'z']
my_list.extend(list_two) # add items from a list to another list
print(my_list)


item  = my_list.pop() # if an index is not specified Pop method removes a list last item
print(my_list)
print(item)

my_list.pop(0)
print(my_list)


my_list.reverse() #list items in reverse
print(my_list)

my_list = [1,23,2,4234,21]
my_list.sort() # sorts items in list (in case of numbers it sorts them from lower to higher)
print(my_list)


my_list = [1, 2, ['x', 'y', 'z']]
print(my_list[2][1]) # This is how you look for an item inside of another list [2] = ['x', 'y', 'z'] and [2][1] = "y"

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List Comprehension
first_col = [row[0] for row in matrix] # what this does is that creates a new list with all item[0] of all lists inside a matrix(thats just a nested list)
print(first_col)
