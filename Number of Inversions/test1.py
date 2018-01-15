# Kaitlyn Stumpf
# Coursera
# Algorithms: Design and Analysis I
# Tim Roughgarden, Stanford
# 01/02/2018

# Start by turning text file into an array of integers.
import os.path, sys

def main():
	fileName = "IntegerArray.txt"
	integerFile = open(fileName, "r")
	strList = integerFile.readlines()

	intList = []

	for num in strList:
		intList.append(int(num.strip()))

	lenList = len(intList)

	count = numInversions(intList, 0, lenList - 1)
	print(count)

def numInversions(intList, low, high):
	count = 0

	# Base case
	if (len(intList) <= 1):
		return 0

	elif low < high:
		# Split the intList in half, putting first half in leftList and 2nd half in rightList
		mid = int(len(intList)/2)
		leftList = intList[:mid]
		rightList = intList[mid:]

		leftCount = numInversions(intList, low, mid)
		rightCount = numInversions(intList, mid + 1, high)
		mergeCount = merge(intList, low, mid, high)
		count = leftCount + rightCount + mergeCount

	return count


def merge(intList, low, mid, high):
	tmp = []

	leftStart = low
	leftEnd = mid
	rightStart = mid + 1
	rightEnd = high

	i = 0
	mergeCount = 0

	while ((leftStart <= leftEnd) and (rightStart <= rightEnd)):
		if intList[leftStart] <= intList[rightStart]:
			tmp[i] = intList[leftStart]
			i += 1
			leftStart += 1
		else:
			tmp[i] = intList[rightStart]
			mergeCount = mergeCount + (leftEnd - leftStart + 1)
			i += 1
			rightStart += 1
	
	if (leftStart > leftEnd):
		for k in range(rightStart, rightEnd):
			tmp[i] = intList[k]
			i += 1
	else:
		for k in range(leftStart, leftEnd):
			tmp[i] = intList[k]
			i += 1

	for k in range (low, high):
		intList[k] = tmp[k - low]

	return mergeCount

main()
