x = open("Input file.txt", "r")
y = open("output.txt", "w")

h_n = {}
parent = {}
while True:
    a = x.readline().split()
    if not a:
        break
    for i in range(2,len(a),2):
        if a[0] not in parent:
            parent[a[0]] = []
            parent[a[0]].append([a[i],int(a[i+1])])
        else:
            parent[a[0]].append([a[i],int(a[i+1])])

    h_n[a[0]] = int(a[1])



queue = []
queue.append(["Arad",h_n["Arad"],0]) 
path = {}
path_cost = {"Arad":0}
flag = False
while queue:
    queue.sort(key = lambda x: x[1]) #Creating a Priority Queue based on h(n)
    current = queue.pop(0)
    g_n = current[2]

    if current[0] == "Bucharest":
        flag = True
        break
    for adj,cost in parent[current[0]]:
        cost = g_n + cost
        f_n = cost + h_n[adj]
        if adj not in path_cost or path_cost[adj] > cost:
            path_cost[adj] = cost
            queue.append([adj,f_n,cost])
            path[adj] = current[0]

if not flag:
    y.write("Path not found")
    
else:      
    total_cost = current[1]
    dest = "Bucharest"
    final_path = []
    while dest:
        final_path.append(dest)
        dest = path.get(dest)
    y.write("Path: ")
    for i in final_path[len(final_path)-1:0:-1]:
        y.write(i + "-> ")
    y.write(final_path[0] + "\n" + "Total Distance: " +str(total_cost)+" km")
x.close()
y.close()    