from math import inf


def maxSubArraySum(array, left, right):
    if (left > right):
        return -inf

    if (left == right):
        return array[left]

    middle = (left + right) // 2

    return max(maxSubArraySum(array, left, middle-1),
               maxSubArraySum(array, middle+1, right),
               maxCrossingSum(array, left, middle, right))


def maxCrossingSum(array, left, middle, right):
    sum = 0
    left_sum = -inf

    for i in range(middle, left-1, -1):
        sum = sum + array[i]

        if (sum > left_sum):
            left_sum = sum

    sum = 0
    right_sum = -inf

    for i in range(middle, right + 1):
        sum = sum + array[i]

        if (sum > right_sum):
            right_sum = sum

    return max(left_sum + right_sum - array[middle], left_sum, right_sum)


def main():
    array = [-4, 5, 7, -6, 10, -15, 3]
    result = maxSubArraySum(array, 0, len(array)-1)
    assert(result == 16)


if __name__ == "__main__":
    main()
