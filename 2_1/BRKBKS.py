numberTest = int(input())


def maxbricks(power, brick):
    summary = 0
    counter = 0
    for i in range(len(brick)):
        tempo = summary + brick[i]
        if power >= tempo:
            summary = summary + brick[i]
            counter += 1
    return int(counter)


for x in range(numberTest):
    bricks = input().split(" ")
    bricks = list(map(int, bricks))
    strength = bricks[0]
    bricks.pop(0)
    hits = 0
    while len(bricks) > 0:
        temp = list(bricks)
        temp.reverse()
        comp1 = maxbricks(strength, bricks)
        comp2 = maxbricks(strength, temp)
        if comp1 > comp2:
            hits += 1
            for x in range(comp1):
                bricks.pop(0)
        else:
            hits += 1
            bricks.reverse()
            for x in range(comp2):
                bricks.pop(0)
    print(hits)
