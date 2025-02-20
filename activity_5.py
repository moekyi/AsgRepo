age = int(input("Please enter your age:"))
if age <= 18:
    numbLessons = 20
else:
    numbLessons = 20 + (age - 18) * 2
print("You need", numbLessons, "driving lessons.")  