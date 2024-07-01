num_of_lists = 6
maxnames_in_group = 6

names = []
number_of_names = int(input("Please enter the number of your names: "))

for i in range(number_of_names):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

Lists = [[] for _ in range(num_of_lists)]

for i in range(number_of_names):
    group_index = i // maxnames_in_group
    if group_index < num_of_lists:
        Lists[group_index].append(names[i])
    else:
        print("You have entered too many names")

for i in range(num_of_lists):
    print(f"Group {i + 1}")
    for name in Lists[i]:
        print(f" {name}")