arr = [3, 6, 8, 2, 0, 1, 784, 2, 14]

def quicksort(A, low, high):
    if low < high:
        p = high//2
        quicksort(A, low, p)
        quicksort(A, p, high)

quicksort(arr, min(arr), max(arr))

print(arr)

def standartSort