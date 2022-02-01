from numpy import test


def mergesort(arr):
    if len(arr) < 2:
        return arr
    h = len(arr) // 2
    arr1 = mergesort(arr[:h])
    arr2 = mergesort(arr[h:])
    print(arr1, arr2)

    sorted = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            sorted.append(arr1.pop(0))
        else:
            sorted.append(arr2.pop(0))
    for item in arr1:
        sorted.append(item)
    for item in arr2:
        sorted.append(item)
    return sorted

def main():
    test_list = [6,1,3,2,7,4,1,5]
    sorted = mergesort(test_list)
    print(sorted)

if __name__ == "__main__":
    main()
