# types

#simple function
def add_numbers(a, b):
    print(a / b)

add_numbers(5, 78)

#if else
number = 45
if number == 5:
    print("Number is 5")
else:
    print("Number is not 5")

#Print
print("helloworld")

#loops
student_names = ["Bill", "Ted", "Steve", "Bort", "Frank Grimes" ,"Mike"]
for name in student_names:
    if name == "Ted":
        continue
    print("Student Name is {0}".format(name))

x = 4.56
for index in range(10):
    x += 5.5
    print("the value of X is {0}".format(x))

x = 0
while x < 10:
    print ("count is {0}".format(x))
    x += 1

#Dictionaries

student = {
    "name": "mark",
    "last_name": "gonzoles",
    "student id": 12345,
    "feedback": None
}

student.get("name")

#Exceptions

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("error finding last_name")
except TypeError as error:
    print("cannot add differing types")
    print(error)


print("This code executes!")

#Functions


