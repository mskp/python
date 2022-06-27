from array import array
from time import time, process_time, sleep

class Sort:

    @staticmethod
    def insertion_sort(arr: array)-> None:

        for i in range(1, len(arr)):
            key: int = arr[i]
            j: int = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

    @staticmethod
    def bubble_sort(arr: array)-> None:
        size = len(arr)

        for i in range(size - 1):
            is_sorted = True

            for j in range(size - i - 1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_sorted = False

            if is_sorted:
                return
    
    @staticmethod
    def selection_sort(arr: array)-> None:
        size: int = len(arr)

        for i in range(size - 1):
            minIndex = i

            for j in range(i + 1, size):

                if arr[j] < arr[minIndex]:
                    minIndex = j

            arr[i], arr[minIndex] = arr[minIndex], arr[i]

if __name__ == "__main__":
    # arr = [23, 56, 78, 1, 90, 6, 43]
    arr: list = [i for i in range(1, 20000)]

    toc = time()
    # Sort.bubble_sort(arr)
    # Sort.insertion_sort(arr)
    Sort.selection_sort(arr)
    # sleep(1)
    tic = time()

    # print(f'{arr}\nTime taken: {tic - toc}')
    print(tic - toc)