# let create  a simple calculator using python

              # method 1 using functions and dictionary

# addition function
def add(x,y):
    return x + y
# subtraction function
def subtract(x,y):
    return x - y

# multiplication function
def multiply(x,y):
    return x * y

# division function
def divide(x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y
calculator = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}
# user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation:")


# what operation user want to perform
for key in calculator:
    print(key)
operation = input("Enter operation: ")
if operation in calculator:
# call the corresponding function based on user input
    result = calculator[operation](num1, num2)
    print("Result:", result)
else:
    print("Invalid operation.")
               # what happens we use values() instead of keys() in the for loop below?
# for value in calculator.values():
#     print(value)
# operation = input("Enter operation: ")
# if operation in calculator:
# # call the corresponding function based on user input
#     result = calculator[operation](num1, num2)
#     print("Result:", result)
# else:
#     print("Invalid operation.")
               # use items() in for loop
# for key, value in calculator.items():
#     print(key, value)
# # test the key and value pairs in the dictionary
# print(calculator.items())
# # operation = input("Enter operation: ")
# # if operation in calculator:
# # # call the corresponding function based on user input
# #     result = calculator[operation](num1, num2)
# #     print("Result:", result)
# # else:
# #     print("Invalid operation.")

                           # method 2 using if statements
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# choice = input("Enter choice (1/2/3/4): ")
# if choice == '1':
#     result = add(num1, num2)
#     print("Result:", result)
# elif choice == '2':
#     result = subtract(num1, num2)
#     print("Result:", result)
# elif choice == '3':
#     result = multiply(num1, num2)
#     print("Result:", result)
# elif choice == '4':
#     result = divide(num1, num2)
#     print("Result:", result)
# else:
#     print("Invalid choice.")


