#variables for the number of lists and the maximum names each list must contain
num_of_lists = 6
maxnames_in_group = 6

#This is a list that will store all inputed names
names = []

#This would prompt the user to input the number of names(and integer value) which he wants to input
number_of_names = int(input("Please enter the number of your names: "))

#A forloop to iterate and store the inputed names
for i in range(number_of_names):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

#thsi initializes a list of empty lists to set of names
Lists = [[] for _ in range(num_of_lists)]

#this assigns the names into the groups
for i in range(number_of_names):
    group_index = i // maxnames_in_group
    if group_index < num_of_lists:
        Lists[group_index].append(names[i])
    else:
        print("You have entered too many names")

#this would print the lists and the names they hold
for i in range(num_of_lists):
    print(f"Group {i + 1}")
    for name in Lists[i]:
        print(f" {name}")
