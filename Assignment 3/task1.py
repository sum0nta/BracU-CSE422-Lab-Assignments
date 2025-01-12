import random

def alpha_beta(node,depth,alpha,beta,max_player):
    if depth == 0:
        return node
    if max_player: 
        best = float('-inf')
        for i in node:
            current = max(best,alpha_beta(i,depth-1,alpha,beta,0))
            best = max(best,current)
            alpha = max(alpha,best)
            if beta <= alpha:
                return alpha
        return best
    else:
        lowest = float('inf')
        for i in node:
            current = min(lowest,alpha_beta(i,depth-1,alpha,beta,1))
            lowest = min(lowest,current)
            beta = min(beta,lowest)
            if beta <= alpha:
                return beta
        return lowest


f  = open("input.txt","r")
f1 = open("output.txt","w")
first_player = int(f.readline())

def create_tree(branching_factor,depth):
    if depth == 0:
        return random.choice([-1,1])
    node = []
    for i in range(branching_factor):
        node.append(create_tree(branching_factor,depth-1))
    return node

branching_factor = 2
depth = 5

current_player = first_player

number_rounds = random.randint(3,10)
winner = []
# Here the first player is always a max player and the result = 1 means the max player won and result = -1 means the min player won
for j in range(number_rounds):   
    tree = create_tree(branching_factor,depth)
    round_winner = alpha_beta(tree,depth,float('-inf'),float('inf'),True)
    
    if round_winner > 0: # If the round is won by the max player
        if current_player == 1: # If the current player is Sub-Zero
            winner.append("Sub-Zero")
        else:
            winner.append("Scorpion")
    else:
        if current_player == 0:
            winner.append("Scorpion")
        else:
            winner.append("Sub-Zero")
    current_player = abs(1 - current_player)

if winner.count("Sub-Zero") > winner.count("Scorpion"):
    f1.write("Winner of the game: Sub-Zero" + "\n")
elif winner.count("Sub-Zero") == winner.count("Scorpion"):
    f1.write("Game is a draw" + "\n")
else:  
    f1.write("Winner of the game: Scorpion" + "\n")

f1.write(f"Total rounds played: {number_rounds}"+ "\n")
for i in range(len(winner)):
    f1.write(f"Winner of Round {i+1} : {winner[i]}" + "\n")

f.close()
f1.close()