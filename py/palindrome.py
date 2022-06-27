def is_palindrome(number: int) -> bool:
    '''returns True if number is palindrome else returns False'''

    reversed: int = 0
    num: int = number

    while num != 0:
        reversed = (reversed*10) + (num%10)
        num //= 10

    return reversed == number

# del is_palindrome

# def is_palindrome(string: str) -> bool:
#     '''returns True if string is palindrome else returns False'''

#     reversed: str = ''

#     for i in range(len(string) - 1, -1, -1):
#         reversed += string[i]

#     return reversed == string

# def is_palindrome_string(string: str) ->bool:
#     result: str = ''
#     for i in range(len(string)):
#         result += string[len(string)-i-1]
#     return string == result

# del is_palindrome

if __name__ == '__main__':
    # print(is_palindrome('madam'))
    print(is_palindrome(2342232))