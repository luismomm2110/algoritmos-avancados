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

# O(log n ) porque no pior dos casos sobe do fundo da raiz ate o fundo


def heapify(array, N, i):
    largest = i
    # pega os filhos ao redor da raiz
    # vai dividir em camadas, onde na quarta camada estara 2*i elementos https://www.happycoders.eu/algorithms/heapsort/
    left = 2*i + 1
    right = 2*i + 2

    # se existe troca e é maior, troca
    if left < N and array[left] > array[largest]:
        largest = left

    # se existe troca e é maior, troca
    if right < N and array[right] > array[largest]:
        largest = right

    # se nao for maior que a raiz, pega
    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        # recursiva no resto a partir do raiz
        heapify(array, N, largest)


def heapSort(array):
    N = len(array)

    # vai ordenar array de forma a estar em maxheap
    for i in range(N//2 - 1, -1, -1):
        heapify(array, N, 0)

    # tempo de execucao vai chamando n vezes o heapify portanto O(n(logn))
    # um a um vai pegando o maximo e heapifica o resto do array
    for i in range(N-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


if __name__ == "__main__":
    main()
