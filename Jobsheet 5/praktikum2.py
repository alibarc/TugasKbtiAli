DAG = {'A':{'C':4,'G':9},
    'G':{'E':6},
    'C':{'D':6,'H':12},
    'D':{'E':7},
    'H':{'F':15},
    'E':{'F':8},
    'F':{'B':5}}

def shortest_path(graph,start,end):
    result = []
    result.append(start)

    while end not in result:
        current_node = result[-1]
        local_max = min(graph[current_node].values())
        for node,weight in graph[current_node].items():
            if weight == local_max:
                result.append(node)
    return result

shortest_path(DAG,'A','B')