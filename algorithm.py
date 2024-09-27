import random
import networkx as nx
import matplotlib.pyplot as plt

n = 12
a, b, c, d, e, f, g, h, i, j, k, m = range(n)
N = [
    {b:1, c:1}, #a
    {a:1, c:1, d:1}, #b
    {a:1, b:1, d:1, e:1}, #c
    {b:1, c:1, e:1, f:1}, #d
    {c:1, d:1, f:1, g:1}, #e
    {d:1, e:1, g:1, h:1}, #f
    {e:1, f:1, h:1, i:1}, #g
    {f:1, g:1, i:1, j:1}, #h
    {g:1, h:1, j:1, k:1}, #i
    {h:1, i:1, k:1, m:1}, #j
    {i:1, j:1, m:1}, #k
    {i:1, k:1} #m
]

#Алгоритм Прима
G = nx.Graph()
print('Алгоритм Прима')
ans = 0
start = random.randint(0, 9)
used = [start]
print('start =', start+1)
for p in range(n-1):
    mn = float('inf')
    pos1 = -1
    pos2 = -1
    for w in used:
        for q in range(n):
            if q in N[w] and N[w][q] < mn and q not in used:
                mn = N[w][q]
                pos1 = w
                pos2 = q
    print(pos1+1, pos2+1)
    G.add_edge(pos1 + 1, pos2 + 1)
    used.append(pos2)
    ans += N[pos1][pos2]
nx.draw(G, with_labels = True)
plt.savefig("graph.png")
print('answer =', ans)

#Алгоритм Краскала
'''print('\nАлгоритм Краскала')
mn = float('inf')
pos1 = -1
pos2 = -1
used = []
for p in range(n):
    for q in range(p+1, n):
        if q in N[p] and N[p][q] < mn:
            mn = N[p][q]
            pos1 = p
            pos2 = q
            used.append(p)
            used.append(q)
print(pos1+1, pos2+1)
ans = N[pos1][pos2]
for p in range(n-2):
    mn = float('inf')
    pos1 = -1
    pos2 = -1
    for w in used:
        for q in range(n):
            if q in N[w] and N[w][q] < mn and q not in used:
                mn = N[w][q]
                pos1 = w
                pos2 = q
    print(pos1+1, pos2+1)
    used.append(pos2)
    ans += N[pos1][pos2]
print('answer =', ans)
'''
