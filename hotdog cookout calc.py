number_of_people = int(input("Enter the number of people: "))
hotdogs_per_person = int(input("Enter the number of hot dogs per person: "))

hotdogs_per_package = 10
buns_per_package = 8

total_hotdogs = number_of_people * hotdogs_per_person

hotdog_packages_needed = total_hotdogs // hotdogs_per_package
hotdog_buns_needed = total_hotdogs // buns_per_package
hotdogs_leftover = total_hotdogs % hotdogs_per_package
buns_leftover = total_hotdogs % buns_per_package

print("Minimum number of packages of hot dogs required =", hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", hotdog_buns_needed)
print("Number of hot dogs left over =", hotdogs_leftover)
print("Number of hot dogs buns left over =", buns_leftover)
