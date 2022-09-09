def main():
    array = [7, 8, 3, 2, 5, 2, 1, 4, 3, 0]

    heapSort(array)

    N = len(array)
    for i in range(N):
        print("%d" % array[i], end=" ")


def open_file(filepath: str):
    names = []
    with open(filepath, "r") as f:
        f.readline()
        for line in f.readlines():
            current_name = [x for x in line.split(",")]
            names.append(current_name[0].strip('"'))
    return sorted(names)



def heapify(array, N, i):
    largest = i
 
    left = 2*i + 1
    right = 2*i + 2

    if left < N and array[left] > array[largest]:
        largest = left

    if right < N and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, N, largest)


def heapSort(array):
    N = len(array)

    for i in range(N//2 - 1, -1, -1):
        heapify(array, N, 0)

    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


if __name__ == "__main__":
    main()
