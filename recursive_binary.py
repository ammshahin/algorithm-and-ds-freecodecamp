def recursive_binary(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2
        if list[mid] == target:
            return True
        elif list[mid] < target:
            return recursive_binary(list[mid + 1:], target)
        else:
            return recursive_binary(list[:mid - 1], target)


def verify(idx):
    if idx:
        print("Target found :", idx)
    else:
        print("Target found :", idx)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result2 = recursive_binary(numbers,10)

verify(result2)

result2 = recursive_binary(numbers,20)

verify(result2)