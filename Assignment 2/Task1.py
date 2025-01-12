import random

def generatePopulation(n,m):
    str1 = ""
    for i in range(n):
        for j in range(m):
            str1+= str(random.choice([0,1]))
    return str1

def crossover(parent1,parent2):
    point = random.randint(0,len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1,child2

def mutation(parent1,parent2):
    offspring = ""
    point = [random.choice([0,1]) for i in range(len(parent1))]
    for i in range(len(point)):
        if point[i] == 1:
            offspring+=parent2[i]
        else:
            offspring+=parent1[i]
    return offspring   
               
def calculateFitness(chromosome,n,m):
    x = [0 for i in range(n)]
    overlap = []

    for i in range(n):
        for j in range(i,n*m,3):
            x[i] += int(chromosome[j])
    consistency = [abs(x[i]-1) for i in range(len(x))]

    for i in range(n):
        total = 0
        for j in range(i*m,(i*m+m)):
            if chromosome[j] == "1":
                 total += 1
        if total == 0:
            overlap.append(0)
        else:
            overlap.append(total-1)

    return sum(overlap)+sum(consistency)

def bestFitness(chromosome1,chromosome2,n,m):
    if calculateFitness(chromosome1,n,m) < calculateFitness(chromosome2,n,m):
        return [calculateFitness(chromosome1,n,m),chromosome1]
    return [calculateFitness(chromosome2,n,m),chromosome2]
def perfectFitness(chromosome1,chromosome2,n,m):
    if calculateFitness(chromosome1,n,m) == 0:
        return [True,chromosome1]
    if calculateFitness(chromosome2,n,m) == 0:
        return [True,chromosome2]
    return [False,'']

f= open("input.txt","r")
f1 = open("output.txt","w")
n,m = [int(i) for i in (f.readline().split())]
best_fitness = [float("inf"),""]
for i in range(100): #Genetic algorithm
    population = []
    for j in range(10):
        population.append(generatePopulation(n,m))
    for x in range(5):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        if bestFitness(parent1,parent2,n,m)[0] < best_fitness[0]:
            best_fitness = bestFitness(parent1,parent2,n,m)
    
        if perfectFitness(parent1,parent2,n,m)[0]:
            f1.write("Total Penalty: 0 \n")
            f1.write(perfectFitness(parent1,parent2,n,m)[1])
            exit()
        
        child1,child2 = crossover(parent1,parent2)
        if perfectFitness(child1,child2,n,m)[0]:
            f1.write("Total Penalty: 0 \n")
            f1.write(perfectFitness(child1,child2,n,m)[1])
            exit()
        if bestFitness(child1,child2,n,m)[0] < best_fitness[0]:
            best_fitness = bestFitness(child1,child2,n,m)

        child1,child2 = mutation(child1,child2), mutation(child2,child1)
        if perfectFitness(child1,child2,n,m)[0]:
            f1.write("Total Penalty: 0 \n")
            f1.write(perfectFitness(child1,child2,n,m)[1])
            exit()
        if bestFitness(child1,child2,n,m)[0] < best_fitness[0]:
            best_fitness = bestFitness(child1,child2,n,m)

f1.write(f"Total Penalty: {best_fitness[0]}")
f1.write(f"\nBest Chromosome: {best_fitness[1]}")
f.close()
f1.close()