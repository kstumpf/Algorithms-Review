
def main():
    fileName = "IntegerArray.txt"
    integerFile = open(fileName, "r")
    strList = integerFile.readlines()

    intList = []

    for num in strList:
        intList.append(int(num.strip()))

    count = countInversions(intList)
    print(count)


def countInversions(list):
    if(len(list) <= 1):
        return list, 0
    else:
        mid = int(len(list)/2)
        left, a = countInversions(list[:mid])
        right, b = countInversions(list[mid:])
        result, c = mergeAndCount(left, right)
        return result, (a + b + c)


def mergeAndCount(left, right):
    result = []
    count = 0
    i,j = 0,0

    while(i < len(left) and j < len(right)):
        if(left[i] > 2*right[j]):
            count += len(left)-i
            j += 1
        else:
            i += 1

    i,j = 0,0                
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while(left[i:] or right[j:]):
        if(left[i:]):
            result.append(left[i])
            i += 1
        if(right[j:]):
            result.append(right[j])
            j += 1
    return result, count


main()