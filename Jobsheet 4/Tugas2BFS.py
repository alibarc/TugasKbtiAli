graph = {
    'A' : ['B'],
    'B' : ['F','G'],
    'C' : ['D'],
    'D' : ['H'],
    'E' : [],
    'F' : ['E'],
    'G' : ['C'],
    'H' : []
}

visited = []
queue = []

def bfs(visited, graph, node, nodedicari):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")
        if(s != nodedicari):
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        else :
            break

print("Hasil penelusuran Node D menggunakan BFS")
bfs(visited,graph,'A','D')