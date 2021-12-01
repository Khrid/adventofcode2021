# day 1 part 1
file = open("day01/input_p1.txt")
lines = file.readlines()
previous = 0
larger = 0
for line in lines:
    iline =  int(line)
    if(iline > previous and previous != 0):
        larger += 1
    previous = iline

print("Day 01 part 1 - How many measurements are larger than the previous measurement?\n " + str(larger))

# day 1 part 2
file = open("day01/input_p2.txt")
lines = [each.strip() for each in file.readlines()]
count = 0
for i in range (3, len(lines)):
    if(int(lines[i-3]) + int(lines[i-2]) + int(lines[i-1]) < int(lines[i]) + int(lines[i-2]) + int(lines[i-1])):
        count += 1
print("Day 01 part 2 - How many measurements are larger than the previous measurement?\n " + str(count))
