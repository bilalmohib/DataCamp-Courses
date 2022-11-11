# Python List
# A list is a way to give a name to a collection of values.
# eg: [1, 2, 3, 4, 5]

# Create a list
my_list = [1, 2, 3, 4, 5]

# float list
float_list = [1.0, 2.0, 3.0, 4.0, 5.0]

# string list
string_list = ['a', 'b', 'c', 'd', 'e']

# mixed list
mixed_list = [1, 2.0, 'a', 'b', True]

# empty list
empty_list = []

# list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Print the list
print(my_list)

### Lists are mutable

# Create a list

# As opposed to int, bool etc., a list is a compound data type; you can group values together:

# a = "is"
# b = "nice"
# my_list = ["my", "list", a, b]

# After measuring the height of your family, you decide to collect some information on the house 
# you're living in. The areas of the different parts of your house are stored in separate variables for 
# now, as shown in the script.
# Instructions
# 100 XP

#     Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room 
#     (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
#     Print areas with the print() function.

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall,kit,liv,bed,bath]

# Print areas
print(areas)

### Create list with different types

# A list can contain any Python type. Although it's not really common, a list can also contain a mix of 
# Python types including strings, floats, booleans, etc.

# The printout of the previous exercise wasn't really satisfying. It's just a list of numbers 
# representing the areas, but you can't tell which area corresponds to which part of your house.

# The code in the editor is the start of a solution. For some of the areas, the name of the corresponding
# room is already placed in front. Pay attention here! "bathroom" is a string, while bath is a variable that represents the float 9.50 you specified earlier.
# Instructions
# 100 XP

#     Finish the code that creates the areas list. Build the list so that the list first contains the 
#     name of each room as a string and then its area. In other words, add the strings "hallway", 
#     "kitchen" and "bedroom" at the appropriate locations.
#     Print areas again; is the printout more informative this time?

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = [hall, kit, "living room", liv, bed, "bathroom", bath]

# Print areas
print(areas)