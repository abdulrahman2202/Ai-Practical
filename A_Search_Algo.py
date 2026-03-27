"""4 - Write a program to find the shortest path using the A search algorithm with a suitable heuristic"""


g = {'A' : 0}
h = {'A':3,'B':2,'C':1,'D':0}
p = {'A' : None}

G = {
    'A': ['B' , 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

o = {'A'}

while o:
    n = min(o, key=lambda x:g[x] + h[x])
    if n == 'D':
        break
    
    o.remove(n)
    for m in G[n]:
        g[m] = g[n] + 1
        p[m] = n
        o.add(m)

path = []

while n is not None:
    path.append(n)
    n = p[n]

print("path: ",path[::-1])