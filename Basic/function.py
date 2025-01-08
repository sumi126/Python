# A function is a block of code which only runs when it is called. In python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHi(name):
    print(f'hello {name}')

sayHi('Sumi')

#Return values
def getSum(n1,n2):
    total = n1 + n2
    return total
num = getSum(5,26)
print('You are',num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression, Very similar to JS arrow functions 

def get(n1,n2): return n1-n2
getSum = lambda n1,n2: n1+n2
print('get',get(5,2),'lamda ', getSum(4,6))

