# name = "Dawid"
# age = 20
# language = "Python"
# nick = "dejviS"
# multiple assigments
name, age, language, nick = ('Dawid' , 20 , "Python" , 'dejviS')
print("Hello my name is " + name)
print("I'm " + age.__str__() + " yeasr old")
print("I trying programming in " + language)
print("My pseudonim is " + nick)
# typ danych
print(type(age))
# rzutowanie
print(str(age))
# argumenty jako pozycje
print('My name is {name} and I am {age}'.format(name=name, age = age))
#f-string 3.6+
print(f'Hello, my name is {name} and I am {age}')
#string methods

s = "hello world"
print(s.capitalize())
print(s.upper())
print(len(s))
print(s.replace('world',"hi"))
#split to list
print(s.split())
#find
print(s.find('r'))