import numpy as np

def counting_sort(a):
    # First, instantiate an appropriately sized array in which to count instances
    basis = min(a)
    counts = [0 for _ in range(max(a)-min(a)+1)]

    # First pass: count the occurences of each integer
    for element in a:
        counts[element-basis] += 1
    
    # Second pass: 
    start_indices = np.concatenate([[0], np.cumsum(counts)[:-1]])
    destination = [0 for _ in range(len(a))]
    for element in a:
        destination[start_indices[element-basis]] = element
        start_indices[element-basis] += 1
    return destination


def main():
    test_array = [1,2,3,4,4,3,2,1,1,2,3,4,2,3,1,4]
    a = counting_sort(test_array)
    print(a)

if __name__ == "__main__":
    main()