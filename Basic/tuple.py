# A tuple is a collection which is ordered and unchangeable. Allows duplicate number
# create tuple 2 types
fruits = ('apple','orange',"grapes")
fruits2 = tuple(('apple','orange',"grapes"))

print(fruits,fruits2)

# single value needs trailing comma for tuple print,
fruits2 = ('apple',)
print(fruits2, type(fruits2))

# can't change value
# fruits[0] = 'pears'

del fruits  #delete tuple print(fruits)

# A set is a collection which is unindexed and unordered. NO duplicate members.
fruits_set = {'apple','orange','mango'} # create set using {}
print('apple' in fruits_set) # check if in set
fruits_set.add('banana') # add set
fruits_set.add('apple')
print('Fruit set ' ,fruits_set)
fruits_set.remove('banana') # remove set
fruits_set.clear() # clear all item in set
del fruits_set # delete set


