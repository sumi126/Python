# A dictionary is a collection which is unordered, changeable and indexed. No duplicate numbers.

#create dictionary
person = {
    'first_name' : 'Samiul',
    'last_name' : 'Bashir',
    'age' : 24
}

# Constructor
person2 = dict(first_name = 'Fatema' , last_name = 'Kotha')

#Get Value
print(person2['first_name'] )
print(person2.get('last_name') )

#add value/ key
person['phone'] = '01964331020'

print(person, type(person))

#Get dict keys and items
print(person.keys(), person.items())

# copy dict
person2 = person.copy()
person2['city'] = 'Rajshahi'
print('person 2' ,person2)

# Remove items
del(person['age'])
person.pop('phone')

print(person)

# clear
person.clear()
print(person)

# get length
print(len(person2))

# list of dict
people = [
    {'name' : 'Sumi' , 'age' : 24},
    {'name' : 'Sami' , 'age' : 23}
]
print(people[1]['name'])