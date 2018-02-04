# Kaitlyn Stumpf
# 01/28/2018

# Algorithms Review
# Dijkstra's Shortest-Path Algorithm

# Input file contains adjacency list of undirected weighted graph,
# with 200 vertices labeled 1 - 200.
# Each row contains the node tuples adjacent to that node, along w length of each edge.

# Run Dijkstra's on this graph, using 1 as source node.
# Compute shortest-path dist between 1 & every node of graph.
# If there is no path between v & 1, dist = 1000000.

# Report shortest-path dist to 7, 37, 59, 82, 99, 115, 133, 165, 188, 197
# Encode distances as comma-separated string of ints.

from collections import defaultdict

def txtToGraph(fileName):
    f = open(fileName)
    lines = f.readlines()

    graph = defaultdict(list)

    for line in lines:
        vals = line.split()
        for edge in vals[1:]:
            tup = tuple(map(int, edge.split(',')))
            graph[int(vals[0])].append(tup)

    # sourceNode = first key in graph
    sourceNode = next(iter(graph.keys()))
    return graph, sourceNode


def shortestPath(graph, sourceNode):
    # Initialize empty array for visited nodes
    # Initialize shortestPaths graph, 
    # Each node contains tuple (dist = 1000000, empty list)
    visited = []
    shortestPaths = {}
    for node in graph.keys():
        shortestPaths[node] = (1000000, [])

    # Add sourceNode to shortestPaths graph & to visited list
    shortestPaths[sourceNode] = (0, [])
    visited.append(sourceNode)

    # While there are still unvisited nodes
    while set(graph.keys() - visited):
        sourceNode, minEdge = -1, ()

        for node in visited:
            for edge in graph[node]:
                # If we've already visited this node, move on.
                if edge[0] in visited:
                    continue
                # If we've found smaller edge, set minEdge equal to it
                # Set sourceNode equal to new node
                if not minEdge or shortestPaths[node][0] + edge[1] < minEdge[1]:
                    minEdge = (edge[0], shortestPaths[node][0] + edge[1])
                    sourceNode = node

        # Update the length of the path, add node to visited list.
        shortestPaths[minEdge[0]] = (minEdge[1], shortestPaths[sourceNode][1] + [minEdge[0]])
        visited.append(minEdge[0])
    return shortestPaths


if __name__ == '__main__':
    graph, sourceNode = txtToGraph('dijkstra.txt')
    paths = shortestPath(graph, sourceNode)

    shortestPath = {}
    for (node, dist) in paths.items():
        shortestPath[node] = dist[0]

    print(shortestPath[7])
    print(shortestPath[37])
    print(shortestPath[59])
    print(shortestPath[82])
    print(shortestPath[99])
    print(shortestPath[115])
    print(shortestPath[133])
    print(shortestPath[165])
    print(shortestPath[188])
    print(shortestPath[197])