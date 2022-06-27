'''6. A website requires a user to input username and password to register.Write a program to check the validity of password given by user.
Following are the criteria for checking password:
A.) At least 1 letter between [a-z].
B.) At least 1 number between [0-9].
C.) At least 1 letter between [A-Z].
D.) At least 1 character from [$#@].
E.) Minimum length of transaction password: 5.
F.) Maximum length of transaction password: 12.
'''

user_name = input('Enter username: ')
password = input('Enter password: ')

if 4 < len(password) < 13:
  lower_count, upper_count, num_count, sp_char_count = 0, 0, 0, 0

  for char in password:
    if char.islower():
      lower_count += 1
    elif char.isupper():
      upper_count += 1
    elif char.isdigit():
      num_count += 1
    elif char in ['$','#','@']:
      sp_char_count += 1

  if lower_count > 0 and upper_count > 0 and num_count > 0 and sp_char_count > 0:
    print('Valid Password')
    
  else:
    print('Invalid Password')

else:
    print('Invalid Password')
