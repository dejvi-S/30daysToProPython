# Create
person = {
    'first_name': 'Dawid',
    'last_name': 'Zając',
    'age': 20
}

#use constructor
#person2 = dict(first_name="Dawid",last_name="Zając", age = 20)
print(person,type(person))

#get value
print(person['first_name'])
print(person.get('last_name'))

#add key/value
person['phone'] = '551-000-123'

# get dict keys
print(person.keys())

#get dict items
print(person.items())

#copy dict
person2 = person.copy()
person2['city'] = 'Lublin'
print(person2)

#remove item
del(person['age'])
person.pop('phone')
print(person)

#clear
person.clear()
print(person)

#get length
print(len(person2))

#list of dict
people = [
    {'name': 'Dawid', 'age': 16},
    {'name': 'Ania', 'age': 20}
]
print(people[1])