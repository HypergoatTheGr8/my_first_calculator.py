# my_first_calculator.py by AceLewis
# todo: Make it work for all floating point numbers too

if 3/2 == 1:  # Because Python 2 does not know maths
    input = raw_input  # Python 2 compatibility

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))

if sign not in operations:
    print("This calculator only supports +, -, /, *")
else:
    operation = operations[sign]
    result = operation(num1, num2)
    print(f"{num1} {sign} {num2} = {result}")

print("Thanks for using this calculator, goodbye :)")
