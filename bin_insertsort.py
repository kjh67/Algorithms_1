def bin_insertsort(a):
    for k in range (1, len(a)):
        # do the binary partitioning
        lb = 0
        ub = k
        to_insert = a[k]

        # aim to get the upper and lower bound to the same position
        while lb != ub:
            midpoint = lb + (ub-lb)//2
            if to_insert >= a[midpoint]:
                lb = midpoint + 1
            else:
                ub = midpoint

        # shuffle lower items up if required
        if lb != k:
            tmp = a[k]
            for j in range(k, lb, -1):
                a[j] = a[j-1]
            a[lb] = tmp
    # return a

def main():
    test_list = [4,2,3,1,6,5]
    bin_insertsort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()
