numberTest = int(input())
for x in range(numberTest):
    bricks = input().split(" ")
    bricks = list(map(int,bricks))
    strength = bricks[0]
    bricks.pop(0)
