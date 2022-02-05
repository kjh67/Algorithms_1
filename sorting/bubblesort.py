def bubblesort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                sorted = False

def main():
    test_list = [4,2,6,1,5,3]
    bubblesort(test_list)
    print(test_list)

if __name__ == "__main__":
    main()