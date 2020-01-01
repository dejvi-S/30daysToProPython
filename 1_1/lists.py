#list
number = [1,2,3,4,5]
# use a constructor
number2 = list((1,2,3,4,5))

print(number, number2)

# get a value
print(number[0])

# get length of list
print(len(number))

# append to list
number.append(8)

print(number)

# remove
number.remove(2)
#insert in pos
number.insert(2,112)
print(number)
#remove with pop
number.pop(2)
#sort
number.sort()
#revesre sort
number.sort(reverse=True)
#reverse
number.reverse()
print(number)