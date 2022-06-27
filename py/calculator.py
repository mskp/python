while True:
    choice: int = int(input(
'''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponentiation
7. Exit
Enter your choice: '''))

    if choice == 7: exit()
    elif choice > 7 or choice < 1: 
        print('\nInvalid choice')
        continue


    first_num: int = int(input('\nEnter first number: '))
    second_num: int = int(input('\nEnter second number: '))

    match choice:
        case 1: 
            print(f'\n{first_num} + {second_num} = {first_num + second_num}')
        case 2: 
            print(f'\n{first_num} - {second_num} = {first_num - second_num}')
        case 3: 
            print(f'\n{first_num} x {second_num} = {first_num * second_num}')
        case 4: 
            print(f'\n{first_num} / {second_num} = {first_num / second_num}')
        case 5: 
            print(f'\n{first_num} % {second_num} = {first_num % second_num}')
        case 6: 
            print(f'\n{first_num} ^ {second_num} = {first_num**second_num}')