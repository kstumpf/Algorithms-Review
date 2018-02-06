# Kaitlyn Stumpf
# 01/28/2018

# Algorithms Review
# Median Maintenance

# Letting xi denote the ith num of the file,
# the kth median mk is defined as the median of the num x1, ..., xk
# So, if k is odd, then mk is ((k + 1)/2)th smallest num among x1, ..., xk
# If k is even, then mk is the (k/2)th smallest num among x1, ..., xk

# Caculate the sum of 10000 medians, modulo 10000 (i.e. only last 4 digits).
# That is, compute (m1 + m2 + ... + m10000)mod10000

import heapq

    
def medianMaintenance(num, minHeap, maxHeap):
    # If the lowHeap is empty, add new num
    if (len(minHeap) == 0):
        heapq.heappush(minHeap, -num)

    else:
        # If new num greater than greatest num in minHeap, add maxHeap
        if num > -minHeap[0]:
            heapq.heappush(maxHeap, num)
            # if more num in maxHeap, add num into minHeap
            if len(maxHeap) > len(minHeap):
                y = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, -y)
        # Else, add to minHeap
        else:
            heapq.heappush(minHeap, -num)
            # If minHeap is more than 1 greater than maxHeap
            if len(minHeap) - len(maxHeap) > 1:
                # add num into maxHeap
                y = -heapq.heappop(minHeap)
                heapq.heappush(maxHeap, y)
    
    return -minHeap[0], minHeap, maxHeap


def main():
    f = open('median.txt')
    lines = f.readlines()
    numList = []

    for line in lines:
        numList.append(int(line))

    medianList = []
    minHeap = []
    maxHeap = []
    medSum = 0
    
    for num in numList:
        median, minHeap, maxHeap = medianMaintenance(num, minHeap, maxHeap)
        medSum += median
        medianList.append(median)

    print(medSum % 10000)


if __name__ == '__main__':
    main()