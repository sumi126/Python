from os import remove

number = {1,2,3,4,5}
number2 = list((6,7,8,9))
print(number, number2)

fruit =['apple','mango','banana','orange']

print("Give me 3rd fruit name: " + fruit[2])
print("Append and remove fruit name: ")
fruit.append('grapes')
print(fruit)
fruit.remove('mango')
print(fruit,'Length: ',len(fruit))
# append and remove by position
fruit.insert(1,'guava')
fruit.pop(3)
print(fruit)
fruit.reverse()
print(fruit)
fruit.sort()
print(fruit)
fruit.sort(reverse=True)
print(fruit)
fruit[2] = 'Nut'
print(fruit)