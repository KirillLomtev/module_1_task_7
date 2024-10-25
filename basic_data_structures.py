grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
average_score = [sum(grades)/ len(grades) for grades in grades]
my_dict = dict(zip(sorted_students, list(average_score)))
print(my_dict)
