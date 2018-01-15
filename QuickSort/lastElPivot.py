# Kaitlyn Stumpf
# 01/02/2018

# QuickSort, using the last element in the list as an array.

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
   p = choosePivot(numList, right)
   numList[-1], numList[0] = numList[0], numList[-1]
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
   Return last element of list as pivot.
   '''
   return numList[-1]

main()