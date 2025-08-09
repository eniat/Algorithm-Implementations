

MAX = 100000
# Data structures for Kosaraju's Algorithm
adj =[[] for _ in range(2* MAX +1)]
adjInv = [[] for _ in range (2* MAX + 1)]
visited = [False] * (2* MAX +1)
visitedInv = [False] * (2* MAX + 1)

s = [] # Stack for processing scc
scc = [0] * (2* MAX + 1)
counter = 1

# Adds directed edges
def addEdges(a, b):
    adj[a].append(b)

# adds directed edges for inverse graoh
def addEdgesInv(a, b):
    adjInv[b].append(a)

# The first DFS pass
def DFS1(i):
    if visited[i]:
        return
    visited[i] = True
    for neigh in adj[i]:
        DFS1(neigh)
    s.append(i)

# The second DFS pass
def DFS2(i):
    if visitedInv[i]:
        return
    visitedInv[i] = True
    for neigh in adjInv[i]:
        DFS2(neigh)
    scc[i] = counter


def isSatisfiable(F):
    global counter

    # Adding a case to check for immediate cotradictions
    for clause in F:
        if len(clause) == 2 and clause[0] == -clause[1]:
            return False

    n = 0
    for clause in F:
        for literal in clause:
            n = max(n, abs(literal))


    # resets adjacency lists and sccs
    for i in range( 1, 2* n + 1):
        adj[i] = []
        adjInv[i] =[]
        visited[i] = False
        visitedInv[i] = False
        scc[i] = 0

    # Creates the implication graph
    for a, b in F:
        addEdges(-a + n, b + n)
        addEdgesInv(-a + n , b+ n)
        addEdges(-b + n, a +n )
        addEdgesInv(-b + n, a +n)

    for i in range(1, 2 *n + 1):
        if not visited[i]:
            DFS1(i)

    while s:
        node = s.pop()
        if not visitedInv[node]:
            DFS2(node)
            counter +=1

    # If a variable and its negation belong to the same scc it is unsatisfiable
    for i in range(1, n+1):
        if scc[i] == scc[i + n]:
            return False
    return True

F = [[1, -2], [2, 1], [-2, -1]]
F2 = [[1,-1]]
F3 = [[1, 2], [-1, 3], [3, -2], [-3, -2]]
F4 = [[1, -2], [-1, 2], [2, 3], [-3, -1]]
F5 = [[1, 2], [-1, -2], [2, -2], [-2, 2]]


print(isSatisfiable(F))
print(isSatisfiable(F2))
print(isSatisfiable(F3))
print(isSatisfiable(F4))
print(isSatisfiable(F5))

