import random
def generatePopulation(n,m):
    str1 = ""
    for i in range(n):
        for j in range(m):
            str1+= str(random.choice([0,1]))
    return str1
f = open("input.txt","r")
n,m = [int(i) for i in (f.readline().split())]
parent1 = generatePopulation(n,m)
parent2 = generatePopulation(n,m)
points = sorted(random.sample(range(len(parent1)), 4))

offspring1 = parent1[0:points[0]] + parent2[points[0]:points[1]] +parent1[points[1]:points[2]] + parent2[points[2]:points[3]] + parent1[points[3]:]

offspring2 = parent2[0:points[0]] + parent1[points[0]:points[1]] +parent2[points[1]:points[2]] + parent1[points[2]:points[3]] + parent2[points[3]:]
print(offspring1,offspring2)
f.close()
