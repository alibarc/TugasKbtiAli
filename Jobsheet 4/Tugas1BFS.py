graph = {
    'A' : ['B','F','E'],
    'B' : ['G'],
    'C' : ['D'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : ['C','H'],
    'H' : []
}

visited = [] #List to keep track of visited nodes.
queue = [] # Initialize a queue



def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Hasil penulusuran graf menggunakan BFS:")
bfs(visited, graph, 'A')