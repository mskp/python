# import numpy as np
# def inverse_arr(arr):
#     inversion = arr.copy()
#     for index, value in enumerate(arr):
#         inversion[value] = index
#     return inversion

def bubblesort_opti(arr):
    ep = len(arr) - 1

    for i in range(ep):
        is_sorted = True
        for j in range(ep - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False

        if is_sorted:
            return arr

def selectionsort(arr):
    ep = len(arr)
    for i in range(ep - 1):
        min_ind = i
        for j in range(i + 1, ep):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [3,4,1,2,0]
    # print(bubblesort(arr))
    print(selectionsort(arr))
    # print(arr)

    # print(inverse_arr(arr))
