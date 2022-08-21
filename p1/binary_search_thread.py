from collections import defaultdict
from threading import Thread

values = {"M": False, "F": False}


def open_file(filepath: str):
    names = []
    with open(filepath, "r") as f:
        f.readline()
        for line in f.readlines():
            current_name = [x for x in line.split(",")]
            names.append(current_name[0].strip('"'))
    return sorted(names)


def binary_search(names, name, gender):
    global values
    start = 0
    end = len(names) - 1

    while (start <= end):
        middle = (start + end)//2
        midpoint = names[middle]

        if (midpoint > name):
            end = middle - 1
        elif (midpoint < name):
            start = middle + 1
        else:
            values[gender] = True
            return
    return


def main():
    target = input("digite o nome pesquisado\n")
    target = target.upper()
    mulheres = open_file("feminino.csv")
    homens = open_file("masculino.csv")

    thread1 = Thread(target=binary_search, args=(mulheres, target, "F"))
    thread2 = Thread(target=binary_search, args=(homens, target, "M"))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(values)


if __name__ == "__main__":
    main()
