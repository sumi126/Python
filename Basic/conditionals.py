# If/ else conditions are used to decide to do something based on something being true or false

x = 1
y = 15
z = 26

# Comparison Operators (== , !=, >, <, >=, <=) - used to compare values

if z > y:
    print(f'{z} is greater than {y}')

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# logical operator( and, or ,not) - used to combine conditional statements 

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

if not(x == y):
    print(f'{x} is not equal to {y}')

# Membership operators ( not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)

# identity operator (is , is not) - compare the objects, not if they are equal, but if they are actually same object, with the same memory location


if x is y:
    print(x is y)

if x is not numbers:
    print(x not in numbers)
    