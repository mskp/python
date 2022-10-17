from math import sqrt
from sys import setrecursionlimit

class Maths:

    @staticmethod
    def is_even(num: int) -> bool:
        return num%2 == 0

    @staticmethod
    def is_odd(num: int) -> bool:
        return not Maths.is_even(num)

    @staticmethod
    def is_prime(num: int) -> bool:
        if num < 2: return False
        
        elif num == 2: return True

        elif num % 2 == 0: return False

        for i in range(3, int(sqrt(num))+1, 2):
            if num%i == 0: return False

        return True
    
    @staticmethod
    def get_max(first: int, second: int, third: int, fourth: int) ->int: 
        max1: int = first if first > second else second
        max2: int = third if third > fourth else fourth
        return max1 if max1 > max2 else max2

    @staticmethod
    def reverse(num: int) -> int:
        reversed: int = 0

        while num != 0:
            reversed = (reversed*10) + (num%10)
            num //= 10
        
        return reversed

    @staticmethod
    def is_palindrome(num: int) -> bool:
        return Maths.reverse(num) == num

    @staticmethod
    def is_armstrong(number: int) -> bool:
        num: int = number
        result: int = 0

        while num != 0:
            remainder: int = num % 10
            result += remainder**3
            num //= 10

        return result == number

    @staticmethod
    def factorial(num: int) -> int:
        return 1 if num == 0 or num == 1 else num*Maths.factorial(num-1)
        
        # if num == 1 or num == 0: return 1

        # else: return num*Maths.factorial(num-1)

    @staticmethod
    def multiplication_table(num: int):
        # for i in range(1, 11):
        #     print(f"{num} x {i} = {num*i}")
        return '\n'.join([f'{num} x {i} = {num*i}' for i in range(1, 11)])
    
    @staticmethod
    def least_common_multiple(num1: int, num2: int) -> int:
        for i in range(max(num1, num2), (num1*num2) + 1, max(num1, num2)):
            if i%num1 == 0 and i%num2 == 0:
                return i


if __name__ == '__main__':
    # print(Maths.is_armstrong(153))
    # setrecursionlimit(20_000)
    # print(Maths.factorial(5))
    # print(Maths.reverse(734))
    # print(Maths.is_prime(23))
    print(Maths.multiplication_table(2156))
    # obj = Maths(3, 4)
    # print(Maths.least_common_multiple(12, 78))
