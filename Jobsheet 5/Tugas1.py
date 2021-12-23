Route = {
    'A': {'B' : 1,'C' : 3,'D' : 7},
    'B': {'D' : 5},
    'C': {'D': 12}
}

def shortestPath(graph,start,end):
    result = []
    result.append(start)

    while end not in result:
        current_node = result[-1]
        local_max = min(graph[current_node].values())
        for node,weight in graph[current_node].items():
            if weight == local_max:
                result.append(node)
    return result


shortestPath(Route,'A','D')