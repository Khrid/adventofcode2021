def main():
    file = open("day03/input.txt")
    lines = [each.strip() for each in file.readlines()]
    part1(lines)
    part2(lines)

# day 2 part 1
def part1(lines):
    bitlen = len(lines[0])
    gamma, epsilon = "",""
    for i in range(0, bitlen):
        cnt = 0
        for line in lines:
            if(str(line[i]) == "1"): cnt += 1
        if(cnt > len(lines) / 2): 
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0" 
            epsilon += "1"
    print("What is the power consumption of the submarine?\n" + str(int(gamma, 2) * int(epsilon, 2)))


# day 2 part 2
def part2(lines):
    bitlen = len(lines[0])
    gamma, epsilon = "",""
    for i in range(0, bitlen):
        cnt = 0
        for line in lines:
            if(str(line[i]) == "1"): cnt += 1
    print("What is the power consumption of the submarine?\n" + str(int(gamma, 2) * int(epsilon, 2)))   

if __name__ == '__main__':
    main()

def getColumn(arr2d, n):
    return [x[n] for x in arr2d]

def most_common(arr1d):
    return 0 if len([i for i in arr1d if int(i) == 0]) > len([i for i in arr1d if int(i) == 1]) else 1

def least_common(arr1d):
    return 0 if len([i for i in arr1d if int(i) == 0]) <= len([i for i in arr1d if int(i) == 1]) else 1



with open("day03/input.txt", 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]
    for x in range(len(lines[0])):
        most_common_res = most_common(getColumn(lines, x))
        lines = [line for line in lines if most_common_res == int(line[x])]
        if len(lines) == 1:
            break
    oxygen = int(lines[0], 2)
with open("day03/input.txt", 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]
    for x in range(len(lines[0])):
        least_common_res = least_common(getColumn(lines, x))
        lines = [line for line in lines if least_common_res == int(line[x])]
        if len(lines) == 1:
            break
    scrubber = int(lines[0], 2)
print(scrubber * oxygen)

