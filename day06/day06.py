def part1():
    print("part1")
    file = open("day06/input.txt")
    line = file.readline()
    fishes = [int(x) for x in line.split(",")]
    day = 0
    target = 256

    fishcounter = [fishes.count(i) for i in range(0,9)]
    print(fishcounter)

    for i in range(0,target):
        # count how many fishes must pop a new one, and removes them from the array
        spawners = fishcounter.pop(0)
        # add that number to the fish at state 6
        fishcounter[6] += spawners
        # add that number of new fish at the end (state 8)
        fishcounter.append(spawners)
    print(sum(fishcounter))

if __name__ == '__main__':
    part1()
