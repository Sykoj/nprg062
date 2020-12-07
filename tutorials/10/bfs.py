from queue import Queue

nodes_count = 5
graph = [ [ -1 ] * nodes_count for _ in range(nodes_count) ]

edges = [ (3,2), (2,1), (1,4), (4,3), (4,5), (5,3) ]

for edge in edges:
    graph[edge[0] - 1][edge[1] - 1] = '-'
    graph[edge[1] - 1][edge[0] - 1] = '-'

# BFS traversal
queue = Queue()
node = 3 - 1

queue.put(node)
graph[node][node] = 'visited'

while not queue.empty():
    node = queue.get()
    
    # Processing:
    print(node + 1)

    for neighbor in range(nodes_count):
        if graph[node][neighbor] == '-' and graph[neighbor][neighbor] != 'visited':
            graph[neighbor][neighbor] = 'visited'
            queue.put(neighbor)      