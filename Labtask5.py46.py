***PROGRAM:01***


name = input("Enter Name: ")
age = int(input("Enter Age: "))
program = input("Enter Program: ")
marks = float(input("Enter Marks: "))

student = (name, age, program, marks)

print("Student Information:")
print(student)


***PROGRAM:02***


sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = 0
spaces = 0
digits = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    if char == " ":
        spaces += 1
    if char.isdigit():
        digits += 1

print("Number of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)


***PROGRAM:03***



employees = []

for i in range(3):
    print("Enter information for Employee", i + 1)

    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\nEmployee Information:")
print(employees)


***PROGRAM:04***


numbers = (10, 15, 20, 25, 30, 35, 40)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
