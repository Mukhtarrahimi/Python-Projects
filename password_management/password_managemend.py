def add_password(user_name, password):
    with open("passwords.txt", "a") as f:
        f.write(f'{user_name} - {password}')
    print('Added')

# running
while True:
    user_input = input('Select your option (v: view, a: add, q: quit): ')
    if user_input.lower() == 'v':
        print('your password are as follow:')
        
    elif user_input.lower() == 'a':
        print('let\'s add a new user_password')
        user_name = input('Enter name: ')
        user_pass = input('Enter password: ')
        add_password(user_name, user_pass)
    elif user_input.lower() == 'q':
        break
    else:
        print('invalid input!')
        continue