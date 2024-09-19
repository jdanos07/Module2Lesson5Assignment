x_value = int(input("Pick a number for \"x\"- " ))
y_value = int(input("Pick a number for \"y\"- "))
operation = input("Do you want to add, subtract, multiply, or divide x & y? ").lower()
calculations = ['add', 'subtract', 'multiply', 'divide']

def addition():
    return x_value + y_value

def subtraction():
   return x_value - y_value

def multiplication():
   return x_value * y_value

def division():
   return x_value / y_value


if operation == 'add':
    print(addition())
elif operation == 'subtract':
    print(subtraction())
elif operation == 'multiply':
    print(multiplication())
elif operation == 'divide':
    try:
        print(division())
    except ZeroDivisionError:
        print('Undefined. Division by 0 is not computable')
else:
    print('Check the spelling, or the operation not supported.' )