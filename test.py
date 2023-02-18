'''def add_node(v):
    if v not in graph:
        graph[v] = []

def add_edge(v1,v2):
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(node,graph):
    visited = set()
    stack = []
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current,end="-->")
            visited.add(current)
            for i in graph:
                stack.append(i)


graph = {}
add_node("A")
add_node("B")
add_node("C")

add_edge("A","B")
add_edge("A","C")
add_edge("B","C")
print(dfs(A, graph))

'''


            
