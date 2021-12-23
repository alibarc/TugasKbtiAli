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

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Hasil penulusuran graf menggunakan DFS:")
dfs(visited,graph,'A')
    