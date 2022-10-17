# import enum
# import string


# # from functools import reduce

# def kth_largest(arr: list[int], k: int) -> int:
#     arr.sort()
#     return arr[len(arr) - k]


# def two_sum(arr: list[int], target: int) -> list[int]:
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i, j]


# def lcm(x: int) -> list[int]:
#     factors = []
#     while x != 1:
#         for i in range(2, x + 1):
#             if x % i == 0:
#                 factors.append(i)
#                 x //= i
#                 break

#     return factors


# if __name__ == '__main__':


# # print(Months(2))
# # for i in Months:
# #     print(Months.name(2))

# # print(lcm(1024))

# # alphabets
# # list_of_letters: list = [letters for letters in string.ascii_letters.lower()]
# # list_of_consonants: list = list(filter(lambda char: char not in 'aeiou' and char not in 'AEIOU',
# # list_of_letters))
# # print(list_of_consonants)

# # reduce function
# # list_of_numbers = [i for i in range(1, 100)]
# # sum_of_numbers = reduce(lambda num1, num2: num1 + num2, list_of_numbers)
# # print(sum_of_numbers)
# # print(kth_largest(list_of_numbers, 50))
# # print(two_sum(list_of_numbers, 50))
# # print(sqrt(36))

# if __name__ == '__main__':
#     # a, b = 6, 7

#     # if a < b:
#     #     print('foo')
#     # elif b < a:
#     #     print('bar')
#     # else:
#     #     print('baz')
#     a, b = 2, 7
#     for i in range(max(a, b), (a*b)+1, max(a, b)):
#         if i % a == 0 and i % b == 0:
#             print(i)
#             break

if __name__ == '__main__':...

    # a=int(input())
    # b=int(input())
    # print('value of a is :',a)
    # print('value of a is :',b)
    # print('After swapping')
    # print('value of a is :',b)
    # print('value of a is :',a)
    
