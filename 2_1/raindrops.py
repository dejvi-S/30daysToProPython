def convert(number):
    words = ['Pling', 'Plang', 'Plong']
    sentence = ''
    if number % 3.0 == 0:
        sentence+=words[0]
    if number % 5.0 == 0:
        sentence+=words[1]
    if number % 7.0 == 0:
        sentence+=words[2]
    if len(sentence) == 0:
        sentence+=str(number)
    print(sentence)
    pass
