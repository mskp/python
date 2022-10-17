from array import array

class Search:
        
    @staticmethod   
    def linear_search(arr: array, value_to_search: int) -> int:
        for i in arr:
            if i == value_to_search:
                return arr.index(i)

        return -1
                
    @staticmethod
    def binary_search(arr: array, value_to_search: int) -> int:
        low: int = 0
        high: int = len(arr) - 1

        while low <= high:
            mid: int = (low + high) // 2

            if arr[mid] > value_to_search:
                high = mid - 1
            
            elif arr[mid] < value_to_search:
                low = mid + 1

            else:
                return mid

        return -1

if __name__ == "__main__":
    arr = [23, 1, 45, 65, 7 , 890, 7]
    print(Search.linear_search(arr, 890))

    arr.sort()
    print(arr) # [1, 7, 7, 23, 45, 65, 890]
    print(Search.binary_search(arr, 890))