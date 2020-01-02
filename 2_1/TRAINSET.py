

numberOfTestCases = input()
for i in range(int(numberOfTestCases)):
    elements = input()
    words = []
    duplicateTF = 0
    for x in range(int(elements)):
        temp = input()
        if temp not in words:
            words.append(temp)

