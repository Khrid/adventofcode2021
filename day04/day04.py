
def score(carte, number):
    print(carte)
    print(number)
    sum = 0
    for l in carte:
        for c in l:
            c = int(c)
            if(c > 0): sum += c
    print(sum*number)

file = open("day04/input.txt")
lines = [each.strip() for each in file.readlines()]

tirage = [int(x) for x in lines[0].split(",")]
carte,cartes = [],[]

for line_carte in [x for x in lines[2:] if x]:
    cartes.append(list(map(int, line_carte.split())))

cartes = [cartes[i*5:(i+1)*5] for i in range(len(cartes)//5)]
cartesbis = cartes.copy()

bingo = False
for number in tirage:
    if(not bingo):
        for carte in cartes:
            if(carte in cartesbis):
                for line in carte:
                    if(number in line):
                        at = line.index(number)
                        line[at] = -1

                        # check if bingo
                        # line is all -1
                        if(all(l == -1 for l in line)): 
                            bingo = True

                        # column is all -1
                        if(not bingo):
                            columnesMatch = True
                            for i in range(len(carte)):
                                if(carte[i][at] != -1):
                                    columnesMatch = False
                            if(columnesMatch):
                                bingo = True
                        
                        if(bingo):
                            if(len(cartesbis) == 1):
                                score(cartesbis[-1], number)
                            else:                            
                                cartesbis.remove(carte)
                                bingo = False