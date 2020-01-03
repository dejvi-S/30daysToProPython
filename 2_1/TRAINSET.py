def sil(n):
    f = lambda x: x * f(x-1) if x != 0 else 1
    return f(n)

numberOfTestCases = input()
for i in range(int(numberOfTestCases)):
    elements = input()
    words = []
    maxElem = 0;
    minElem = 0;
    for x in range(int(elements)):
        temp = input()
        if temp not in words:
            words.append(temp)
    maxElem = len(words)
    words = [word[:-2] for word in words]
    words = list(set(words))
    minElem = len(words)
    combin = (sil(maxElem) / pow(2,(maxElem-minElem)))
    print(combin)


