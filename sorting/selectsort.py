def selectsort(a):
    for i in range(0, len(a)):
        smallest = i
        for j in range(i+1, len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]

def main():
    test_list = [5,4,3,2,1]
    selectsort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()