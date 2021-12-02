# day 2 part 1
file = open("day02/input.txt")
lines = [each.strip() for each in file.readlines()]
hpos,depth= 0,0
for line in lines:
    direction,units = line.split()
    if(direction == "forward"): hpos += int(units)
    if(direction == "down"): depth += int(units)
    if(direction == "up"): depth -= int(units)
print("Day 2 part 1 - What do you get if you multiply your final horizontal position by your final depth?\n" + str(depth*hpos))
    
# day 2 part 2
file = open("day02/input.txt")
lines = [each.strip() for each in file.readlines()]
hpos,depth,aim = 0,0,0
for line in lines:
    direction,units = line.split()
    if(direction == "forward"): 
        hpos += int(units)
        depth += aim * int(units)
    if(direction == "down"): 
        #depth += int(units)
        aim += int(units)
    if(direction == "up"): 
        #depth -= int(units)
        aim -= int(units)
    #print(line + " : hpos " + str(hpos) + " // depth " + str(depth) + " // aim " + str(aim))
print("Day 2 part 2 - What do you get if you multiply your final horizontal position by your final depth?\n" + str(depth*hpos))