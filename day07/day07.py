file = open("day07/input.txt")
crabs = [int(x) for x in file.readlines()[0].split(",")]
min,max = min(crabs),max(crabs)
minmov,crabi = -1,-1
for i in range(min, max):
    mov = 0
    for crab in crabs:
        m = abs(crab - i)
        #mov += m #p1
        mov += int((m*m +m)/2) #p2
    if(minmov == -1 or minmov > mov): 
        minmov = mov
        crabi = i
print(minmov, crabi)