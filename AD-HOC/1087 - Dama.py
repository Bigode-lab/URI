x1, y1, x2, y2 = (int(x) for x in input().split())
while not(x1 == x2 and y1 == y2 and x1 == 0):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if dx == dy and dx == 0:
        print(0)
    elif dx != dy and dx and dy != 0:
        print(2)
    else:
        print(1)
    x1, y1, x2, y2 = (int(x) for x in input().split())