print("Hello Word")
x = 56
y = 3.8
print(round(x/y))
name,age = ("Sumi",24)
# concatenate only string, so we need typecast to use int, int,double, float convert to string is must for concatenating.
print("Hello I'm "+ name + " I'm "+str(age))
# String formating
#argument position
print('Hello I am  {name} and  I am {age}'.format(name=name, age=age))
# f- string
print(f'Hello I am  {name} and  I am {age}')
s = 'hello world'
print("Capitalize "+s.capitalize())
print('Upper '+s.upper())
print('Lower ' +s.lower())
print('Swap case ' + s.swapcase())
print('Length s: ')
print(len(s))
print('Replace: ' + s.replace('world','everyone'))
print('Count o: ')
print(s.count('o'))
print(s.startswith('h'))
print(s.endswith('d'))
print(s.split())
print('find r: ')
print( s.find('r'))
# space is not acceptable for alphanumeric or alphabetic
print('Is all alphanumeric? ')
print(s.isalnum())
print('Is all alphabetic? ')
print(s.isalpha())
print('Is all alphanumeric? ')
print(s.isnumeric())
