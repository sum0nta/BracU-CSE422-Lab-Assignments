import random

def alpha_beta(node,depth,alpha,beta,max_player):
    if depth == 0:
        return node
    if max_player:
        best = float('-inf')
        for i in node:
            current = max(best,alpha_beta(i,depth-1,alpha,beta,False))
            best = max(best,current)
            alpha = max(alpha,best)
            if beta <= alpha:
                return alpha
        return best
    else:
        lowest = float('inf')
        for i in node:
            
            current = min(lowest,alpha_beta(i,depth-1,alpha,beta,True))
            lowest = min(lowest,current)
            beta = min(beta,lowest)
            if beta <= alpha:
                return beta
        return lowest
import random

def magic(node,depth,alpha,beta,max_player):
    if depth == 0:
        return node
    if max_player:
        best = float('-inf')
        for i in node:
            if not i:
                continue
            current = max(best,magic(i,depth-1,alpha,beta,False))
            best = max(best,current)
            alpha = max(alpha,best)
            if beta <= alpha:
                break
        return best
    else:
        lowest = float('-inf')
        for i in node:
            if not i:
                continue
            current = max(lowest,magic(i,depth-1,alpha,beta,True))
            lowest = max(lowest,current)
            beta = max(beta,lowest)
            if beta <= alpha:
                break
        return lowest


f  = open("input1.txt","r")
f1 = open("output1.txt","w")

nodes = [3,6,2,3,7,1,2,0]
x = 0
def create_tree(branching_factor,depth):
    global x
    if depth == 0:
        x += 1
        return nodes[x-1]

    node = []
    for i in range(branching_factor):
        node.append(create_tree(branching_factor,depth-1))
    return node

branching_factor = 2
depth = 3
tree = create_tree(branching_factor,depth)
magic_value = magic(tree,depth,float('-inf'),float('inf'),1)
alpha_beta_value = alpha_beta(tree,depth,float('-inf'),float('inf'),1)
c = int(f.readline())


if (magic_value-c) > alpha_beta_value:
    f1.write(f"The new minimax value is {magic_value-c}. Pacman goes right and uses dark magic")
else:
    f1.write(f"The new minimax value is {alpha_beta_value}. Pacman does not use dark magic")

f.close()
f1.close()