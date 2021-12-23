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

visited = set()
hasil = []

def dfs(visited, graph, node, nodedicari):
    if node not in visited:
        print(node, end=" ")
        if node != nodedicari:
            visited.add(node)
            for neighbour in graph[node]:
                if nodedicari not in hasil:
                    dfs(visited, graph, neighbour, nodedicari)
            return
        else :
            hasil.append(node)


print("Hasil penelusuran Node D menggunakan DFS")
dfs(visited,graph,'A','D')