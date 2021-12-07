file = open("day05/input.txt")
lines = [each.strip() for each in file.readlines()]
#print(lines)
size = 1000
grid = [ [0]*size for i in range(size)]
crossings = 0
for line in lines:
    xy = ([each.split(",") for each in line.split(" -> ")])
    x1 = int(xy[0][0])
    y1 = int(xy[0][1])
    x2 = int(xy[1][0])
    y2 = int(xy[1][1])
    if(x1 == x2 or y1 == y2 or (abs(x2 - x1) == abs(y2 - y1))):
        if(x1 == x2):
            for i in range(min(y1,y2), max(y1,y2)+1):
                grid[i][x1] += 1
        elif(y1 == y2):
            for i in range(min(x1,x2), max(x1,x2)+1):
                grid[y1][i] += 1
        elif(abs(x2 - x1) == abs(y2 - y1)):
            cx = 1 if x2 > x1 else -1
            cy = 1 if y2 > y1 else -1
            for i in range(abs(x2 - x1) + 1):
                grid[cy*i + y1][cx*i + x1] += 1


for i in range(len(grid[0])):
    #print(grid[i])
    for j in range(len(grid[i])):
        if(grid[i][j] > 1): crossings += 1
print(crossings)
