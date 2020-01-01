fruits = ('Apples')
fruits2 = tuple(('Apples',))
#single vaule needs ','
print(fruits, fruits2)
print(fruits2, type(fruits2))

# get value
print(fruits2[0])

# tuples can't be changed
# delete tuples
#del fruits2
print(len(fruits2))
# set - unique items only
# Create set
fruits_set = {'Apples', 'Oranges' , 'Mango'}

#check if in set
print('Apples' in fruits_set)

#add
fruits_set.add('Grape')
print(fruits_set)

#remove
fruits_set.remove('Grape')
print(fruits_set)

#clear set
fruits_set.clear()

print(fruits_set)

# del
del fruits_set