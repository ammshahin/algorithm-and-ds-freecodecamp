def linear_search(lst, target):
    for _ in range(0, len(lst)):
        if lst[_] == target:
            return _+1
    return None


def verify(idx):
    if idx is not None:
        print("Target found at: ", idx)
    else:
        print("target not found!")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result2 = linear_search(numbers, 8)

verify(result2)
