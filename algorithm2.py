import networkx as nx
import matplotlib.pyplot as plt

n = 12
a, b, c, d, e, f, g, h, i, j, k, m = range(n)
N = [
    {c, h}, #a
    {e, g, i}, #b
    {a}, #c
    {k}, #d
    {b, h, j}, #e
    {g}, #f
    {b, f, k}, #g
    {a, e, m}, #h
    {b}, #i
    {e}, #j
    {d, g}, #k
    {h} #m
]

#Код Прюфера
code = []
for w in range(n-2):
    for q in range(n):
        if len(N[q]) == 1:
            z = N[q].pop()
            code.append(z+1)
            N[z].remove(q)
            break
print('Код Прюфера:', code, end = '\n')

#Обратный код Прюфера
G = nx.Graph()

n = 8
code = [5, 4, 3, 2, 1, 1]
print('Обратный код Прюфера:', code, end = '\n')
pendant = []
for i in range(1, n+1):
    if i not in code:
        pendant.append(i)
for i in range(n-2):
    print(code[i], '-', pendant[0])
    G.add_edge(code[i], pendant[0])
    pendant.pop(0)
    if code[i] not in code[i+1:n-2]:
        pendant.insert(0, code[i])
print(pendant[0], '-', pendant[1])
G.add_edge(pendant[0], pendant[1])

nx.draw(G, with_labels = True)
plt.savefig("graph.png")