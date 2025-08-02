import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_PATH = os.path.join(BASE_DIR, 'passwords.txt')

def add_password(user_name, password):
    with open(FILE_PATH, 'a') as f:
        f.write(f'{user_name} - {password}\n')
    print('Added')
    
def view_password():
    try:
        with open(FILE_PATH, 'r') as f:
            for item in f:
                item = item.strip()
                user_name, user_pass = item.split('-')
                print(f'USERNAME: {user_name} - PASSWORD: {user_pass}')
    except:
        print('No passwords saved')
        

# running
while True:
    user_input = input('Select your option (v: view, a: add, q: quit): ')
    if user_input.lower() == 'v':
        print('your password are as follow:')
        view_password()
        
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