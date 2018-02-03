# Kaitlyn Stumpf
# 01/22/2018
# Strongly Connected Components

import sys
import threading

# Input file contains the edges of a directed graph.
# Vertices are labeled pos int from 1 - 875714
# Every row contains 2 vertices, indicates an edge between them
# Vertex label in 1st column is the tail
# Vertex label in 2nd column is the head
# Edges are directed from 1st column vertex to 2nd

# Return the sizes of the 5 largest SCCs,
# in dec order of sizes, separated by commas.
# If the algo finds less than 5, return 0 for the others

# Memory must be managed carefully

def txtToGraphs(fileName):
    '''
    Reads in input file.
    Returns graph and reversed graph, implemented w adjacency lists.
    '''
    f = open(fileName)
    lines = f.readlines()
    
    adjlist = []
    revAdjList = []
    
    for line in lines:
        tail, head = map(int, line.split())
        maxVertex = max(tail, head)
        
        # Ensure the two lists are still the appropriate size,
        # based off of the new vertices.
        if len(adjlist) < maxVertex:
            diff = maxVertex - len(adjlist)
            adjlist.extend([] for i in range(diff))
            revAdjList.extend([] for i in range(diff))

        # At the tail index, append the head
        adjlist[tail-1].append(head-1)
        # At the head index, append the tail
        revAdjList[head-1].append(tail-1)
            
    return adjlist, revAdjList


def DFSLoop1(revGraph, n):
    '''
    Takes revGraph, length of graph (# nodes)

    Initialize time (# nodes processed) equal to 0.
    Initialize exploredList as False for all nodes.
    Initialize list sortedByFinishingTime, empty.

    Call DFS on each node.

    Returns list sorted by finishing time.
    '''
    t = 0
    exploredList = [False]*n
    sortedByFinishingTime = [None]*n
    
    for i in reversed(range(n)):
        if not exploredList[i]:
            sortedByFinishingTime, t = DFS1(revGraph, i, t, exploredList, sortedByFinishingTime)
    return sortedByFinishingTime
                        
            
def DFS1(revGraph, i, t, exploredList, sortedByFinishingTime):
    '''
    Takes revGraph, current node, time (# nodes processed), list of explored nodes, and sortedByFinishingTime.

    Current node i is marked explored.
    For each arc (i,j) in revGraph, if not explored, recurse.

    Returns list of nodes, sorted by finishing time.
    '''
    
    exploredList[i] = True
    
    for j in revGraph[i]:
        if not exploredList[j]:
            sortedByFinishingTime, t = DFS1(revGraph, j, t, exploredList, sortedByFinishingTime)
    
    sortedByFinishingTime[t] = i
    t += 1
    return sortedByFinishingTime, t
    
    
def DFSLoop2(graph, n, sortedByFinishingTime):
    '''
    Initialize exploredList as False for all nodes.
    Create empty list sccList, to hold 5 largest SCCs.

    For each node in list sorted by finishing time,
        we initialize sccSize to 0.
        we collect all members of next SCC using DFS.

    Returns list of all SCC sizes.
    '''
    exploredList = [False]*n
    sccList = []
    
    for i in reversed(range(n)):
        if not exploredList[sortedByFinishingTime[i]]:
            sccSize = 0
            sccSize = DFS2(graph, sortedByFinishingTime[i], sccSize, exploredList)
            sccList.append(sccSize)
        
    return sccList
    
    
def DFS2(graph, i, sccSize, exploredList):
    '''
    Takes graph, node i, size of current SCC, and list of explored nodes.

    Current node i is marked explored.
    For each arc (i,j) in revGraph, if not explored, recurse.

    Returns size of current SCC.
    '''
    exploredList[i] = True
    
    for j in graph[i]:
        if not exploredList[j]:
            sccSize = DFS2(graph, j, sccSize, exploredList)
    
    sccSize += 1
    return sccSize
    

def kosaraju(graph, revGraph):
    '''
    Initialize variables.

    Run first DFS loop on reverse graph.
    This will resort the list based on finishing times, to discover sink SCC.

    Run second DFS loop on graph.
    Don't need to compute finishing times in 2nd pass.
    In 2nd pass, keep track of leaders (vertex from which DFS was called that first discovered v)

    Returns list of all SCC sizes.
    '''
    exploredList = None
    leader = None
    sccSize = 0

    sortedByFinishingTime = DFSLoop1(revGraph, len(graph))
    sccList = DFSLoop2(graph, len(graph), sortedByFinishingTime)
    
    return sccList


def main():
    '''
    Create graph and reversed graph, by calling txtToGraphs
    Run Kosaraju's algorithm to find 5 largest SCCs.
    Print out 5 largest SCCs in descending order.
    '''
    graph, revGraph = txtToGraphs('SCC.txt')
    sccList = kosaraju(graph, revGraph)
    
    strSCCList = []
    for sccSize in sorted(sccList)[::-1][:5]:
        strSCCList.append(str(sccSize))

    print(','.join(strSCCList))


# Looked up online for help.
# This helps manage memory
if __name__ == '__main__':
    # Specify stack size to be used for subsequently created threads
    # B/c OSX ulimit set to 64MB, anything higher is stack overflow
    # ulimit = # of open file descriptors per process
    threading.stack_size(67108864) # 64MB stack
    # Set the total stack depth
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    # Instantiate new thread obj
    # The target function is our main function
    thread = threading.Thread(target = main)
    # Run the program at the target function
    thread.start()