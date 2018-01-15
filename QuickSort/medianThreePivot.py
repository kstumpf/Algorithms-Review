# Kaitlyn Stumpf
# Coursera
# Algorithms: Design and Analysis I
# Tim Roughgarden, Stanford

#Programming  Assignment #3 - Pt 3
# 01/02/2018

# Start by turning text file into an array of integers.

import statistics

def main():
   '''
   Turn the text file into an list of integers.
   Then, call quickSort, to sort the list.
   '''
   fileName = "QuickSort.txt"
   integerFile = open(fileName, "r")
   strList = integerFile.readlines()

   intList = []

   for num in strList:
      intList.append(int(num.strip()))

   #intList = [7, 5, 4, 1, 3, 6, 2, 8]
   sortedList = []
   sortedList, count = quickSort(intList, 0, len(intList) - 1)
   print(count)


def partition(numList, left, right):
   '''
   Partition the list around the pivot p, found with choosePivot.
   Switch pivot (first el of list) with it's actual location in the list.
   Return the pivot p.
   '''
   p, pIndex = choosePivot(numList, right)
   numList[pIndex], numList[0] = numList[0], numList[pIndex]
   p = numList[0]
   i = 1
   for j in range(1, len(numList)):
      if numList[j] < p:
         numList[j], numList[i] = numList[i], numList[j]
         i = i + 1
   numList[0], numList[i - 1] = numList[i - 1], numList[0]
   return i - 1


def quickSort(numList, first, last):
   '''
   Base Case: If length of list is 1, return the list, and add nothing to the count.
   Recursive Step: Split the list into left and right sides, around pivot p,
      and recurse on each side of the list.
      Return the list, and the number of comparisons (with left and right counts).
   '''
   if len(numList) <= 1:
      return numList, 0
   else:
      comparisons = len(numList) - 1
      p = partition(numList, first, last)
      numList[:p], leftCount = quickSort(numList[:p], first, p)
      numList[p + 1:], rightCount = quickSort(numList[p + 1:], p + 1, last)
      return numList, comparisons + leftCount + rightCount
   

def choosePivot(numList, lenList):
   '''
   Return median element.
   '''
   return medianOfThree(numList, 0, lenList - 1)


def medianOfThree(numList, left, right):
   '''
   Return the median, given 3 el.
   '''
   # Depending on if length of list is even or odd, find middle index
   if len(numList) % 2 == 0:
      med = len(numList) // 2 - 1
   else:
      med = len(numList) // 2
   medList = [numList[left], numList[med], numList[-1]]
   # Find the median, out of the first, middle, and last el
   med = statistics.median(medList)
   medIndex = medList.index(med)
   return med, medIndex


main()