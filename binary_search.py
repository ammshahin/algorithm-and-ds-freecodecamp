def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = list[mid] + 1
        else:
            last = list[mid] - 1
    return None


def verify(idx):
    if idx is not None:
        print("Target found at: ", idx)
    else:
        print("target not found!")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result2 = binary_search(numbers, 11)

verify(result2)