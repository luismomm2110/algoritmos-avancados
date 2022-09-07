from collections import defaultdict


def open_file_with_dict(filepath):
    dict_names = defaultdict(lambda: False)
    with open(filepath, "r") as f:
        f.readline()
        for line in f.readlines():
            current_name = [x for x in line.split(",")]
            dict_names[current_name[2]] = current_name[0].strip('"')
    return dict_names


def open_file(filepath: str):
    names = []
    with open(filepath, "r") as f:
        f.readline()
        for line in f.readlines():
            current_name = [x for x in line.split(",")]
            names.append(current_name[0].strip('"'))
    return sorted(names)


def binary_search(names, name):
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
            return True
    return False


def main():
    target = input("digite o nome pesquisado\n")
    target = target.upper()
    mulheres = open_file("feminino.csv")
    homens = open_file("masculino.csv")

    if (target in open_file_with_dict("feminino.csv").values()):
        print(target + " esta entre os nomes mais comuns de mulheres")
    else:
        print(target + " nao esta entre os nomes mais comuns de mulheres")

    if (binary_search(mulheres, target)):
        print(target + " esta entre os nomes mais comuns de mulheres")
    else:
        print(target + " nao esta entre os nomes mais comuns de mulheres")

    if (binary_search(homens, target)):
        print(target + " esta entre os nomes mais comuns de homens")
    else:
        print(target + " nao esta entre os nomes mais comuns de homens")


if __name__ == "__main__":
    main()
