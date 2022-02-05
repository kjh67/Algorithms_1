def partition(a, i_start, i_end):
    pivot = i_end - 1
    left = i_start
    right = pivot

    assert(i_end - i_start >= 2)

    while left < right:
        while left < right and a[left] <= a[pivot]:
            left += 1
        while left < right and a[right - 1] > a[pivot]:
            right -= 1
        
        # both pointers have been halted: need to swap items if not done
        if left < right:
            assert(right - left >= 2)
            a[left], a[right-1] = a[right-1], a[left]
            left += 1
            right -= 1
        
    # put the pivot in beween the two sets of elements
    a[pivot], a[right] = a[right], a[pivot]
        
    # the right pointer is now the pivot position
    return right


def quicksortSubArray(a, i_left, i_right):
    if i_right - i_left < 2:
        return
    
    pivot = partition(a, i_left, i_right)
    quicksortSubArray(a, i_left, pivot)
    quicksortSubArray(a, pivot + 1, i_right)


def quicksort(a):
    quicksortSubArray(a, 0, len(a))


def main():
    test_array = [8,2,5,1,6,2,3,6,2,3,9,33,2]
    quicksort(test_array)
    print(test_array)

if __name__ == "__main__":
    main()
