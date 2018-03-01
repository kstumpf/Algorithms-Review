from bisect import bisect_left, bisect_right

# Kaitlyn Stumpf
# 02/10/2018

# Algorithms Review
# 2Sum

# Input: Unsorted array of n int. Target sum t.
# Goal: Determine whether or not there are two # x, y in A with x + y = t
# Insert el of A into hashtable H.
# For each x in A, lookup t - x in H.

def main():
    f = open("2Sum.txt")
    lines = f.readlines()

    nums = set()
    for line in lines:
        nums.add(int(line))

    arr = sorted(nums)

    print(twoSum(arr))


def twoSum(arr):
    vals = set()

    for num in arr:
        low = bisect_left(arr, -10000 - num)
        high = bisect_right(arr, 10000 - num)
        for pairNum in arr[low:high]:
            if pairNum != num:
                vals.add(num + pairNum)
    return len(vals)

if __name__ == "__main__":
    main()