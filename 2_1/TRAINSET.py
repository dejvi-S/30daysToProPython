#make functions! clear code
numberOfTestCases = input()
for i in range(int(numberOfTestCases)):
    elements = input()
    wordsTrue = []
    wordsFalse = []
    for x in range(int(elements)):
        temp = input()
        if temp[(len(temp)-1)] == str(1):
            wordsTrue.append(temp)
        else:
            wordsFalse.append(temp)
    wordsTrue = [wordT[:-2] for wordT in wordsTrue]
    wordsFalse = [wordF[:-2] for wordF in wordsFalse]
    dictTrue = dict()
    dictFalse= dict()
    for word in wordsTrue:
        if word not in dictTrue:
            dictTrue[word] = 1
        else:
            dictTrue[word] += 1
    for word in wordsFalse:
        if word not in dictFalse:
            dictFalse[word] = 1
        else:
            dictFalse[word] += 1
    print(wordsTrue)
    print(wordsFalse)
    del wordsTrue
    del wordsFalse
    print(dictFalse)
    print(dictTrue)
    for word in



