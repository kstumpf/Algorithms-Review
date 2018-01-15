# Kaitlyn Stumpf
# 01/02/2018

# Algorithm Review:
# This algorithm will count the number of inversions in a text file,
# where the ith row of the file represents the ith element.

# This is a divide-and-conquer algorithm.


def main():
   '''
   Turn the text file into an list of integers.
   Then, call numInversions, to find the number of inversions in the list.
   '''
   fileName = "IntegerArray.txt"
   integerFile = open(fileName, "r")
   strList = integerFile.readlines()

   intList = []

   for num in strList:
      intList.append(int(num.strip()))

   count = numInversions(intList)
   print(count)


def numInversions(intList):
   '''
   Recursively counts the number of inversions in "intList".

   Base Case: If the length of the list is 1, return the list and do not add anything to the count.
   Recursive Step: If the length of the list > 1, 
      divide the list in two and recurse on the two halves.
      Then, merge the two halves together.

   Returns the list of integers, and the number of inversions.
   '''
   listLength = len(intList)

   if listLength > 1:
      mid = listLength//2

      leftList = intList[:mid]
      rightList = intList[mid:]
      leftList, leftCount = numInversions(intList[:mid])
      rightList, rightCount = numInversions(intList[mid:])
      mergedList, mergedCount = merge(leftList, rightList)
      return mergedList, leftCount + rightCount + mergedCount
   else:
      return intList, 0


def merge(leftList, rightList):
   '''
   Merge the leftList and rightList into a single sorted list.
   '''
   mergeCount = 0
   mergedList = []

   # While neither the leftList nor the rightList is empty
   while leftList and rightList:
      # If left el <= right el, add left el to new list, remove from leftList.
      if leftList[0] <= rightList[0]: 
         mergedList.append(leftList.pop(0)) 
      # If left el > right el, increase inversion count by 1,
      # append right el to new list, remove from rightList.
      else: 
         mergeCount += len(leftList)
         mergedList.append(rightList.pop(0)) 

   # Add the remaining el in either list to mergedList.
   mergedList  += leftList + rightList    
   return mergedList, mergeCount

main()