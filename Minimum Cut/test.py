# Kaitlyn Stumpf
# Coursera
# Algorithms: Design and Analysis I
# Tim Roughgarden, Stanford

#Programming  Assignment #4 - MinCut
# 01/02/2018

# Start by turning text file into an array of integers.
# Find min cut using Karger's randomized contraction algorithm.
from random import randint


def main():
   fileName = "MinCut.txt"
   integerFile = open(fileName, "r")
   strList = integerFile.readlines()

   intList = []

   for line in strList:
      lineList = [int(n) for n in line.split()]
      intList.append(lineList)

   #for line in intList:
   #   print(line)
   #repeatedTrials(intList, 100)
   minCut(intList)


def repeatedTrials(intList, numTrials):
   i = 0
   count = 10000
   while i < numTrials:
      minCutNum = minCut(intList)
      if  minCutNum < count:
         count = minCut
      i = i + 1
   return count



def minCut(intList):
   #First, we need to extract the edges from the data
   edgeList = []
   nodeList = []
   for lineList in intList:
      nodeList.append(lineList[0])
      tempList = []
      # Loop through all vertices connected to vertex label
      for temp in range(1, len(lineList)):
         tempList = [lineList[0], lineList[temp]]
         flag = 0
         # If this edge (u, v) is already in the edge list, set the flag to 1
         for ad in edgeList:
            if ad == tempList:
               flag = 1
         # If the edge (u, v) is not in the edge list, append it
         if flag == 0:
            edgeList.append([[lineList[0]], lineList[temp]])

   # Karger min cut algorithm
   while (len(nodeList) > 2):
      val = randint(0, (len(edgeList) - 1))
      targetEdge = edgeList[val]
      print(targetEdge)
      replaceWith = targetEdge[0]
      shouldReplace = targetEdge[1]
      for edge in edgeList:
         if (edge[0] == shouldReplace):
            edge[0] == replaceWith
         if (edge[1] == shouldReplace):
            edge[1] = replaceWith
      if targetEdge in edgeList:
         edgeList.remove(targetEdge)
      if shouldReplace in nodeList:
         nodeList.remove(shouldReplace)

      for edge in edgeList:
         if edge[0] == edge[1]:
            edgeList.remove(edge)

   print(len(edgeList))
   return(len(edgeList))


main()