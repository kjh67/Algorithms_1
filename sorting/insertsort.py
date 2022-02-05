def insertsort(a):
    for i in range(1, len(a)):
        # one new assignment outside the loop
        to_insert = a[i]
        j = i - 1
        # replaced while j >= 0 and a[j] > a[j+1] with:
        while j >= 0 and a[j] > to_insert:
            # two assignments requires inside the loop instead of 4 
            # (assuming that swap() performs 3 assignments)
            a[j + 1] = a[j]
            j -= 1
        # one additional assignment outside the loop
        a[j+1] = to_insert

def main():
    test_list = [5,4,3,2,1]
    insertsort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()