import os
from cryptography.fernet import Fernet

# write_key
def write_key():
    key = Fernet.generate_key()  
    with open('./mykey.key', 'wb') as f:
        f.write(key)

if not os.path.exists('./mykey.key'):
    write_key()

# load_key
def load_key():
    with open('./mykey.key', 'rb') as f:
        return f.read()

key = load_key()
fernet = Fernet(key)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'passwords.txt')

# add_password
def add_password(user_name, password):
    encrypted_pass = fernet.encrypt(password.encode()).decode()
    with open(FILE_PATH, 'a') as f:
        f.write(f'{user_name}|{encrypted_pass}\n')
    print('Added')

# view_password
def view_password():
    try:
        with open(FILE_PATH, 'r') as f:
            for item in f:
                item = item.strip()
                if not item:
                    continue
                user_name, encrypted_pass = item.split('|')
                password = fernet.decrypt(encrypted_pass.encode()).decode()
                print(f'USERNAME: {user_name.strip()} | PASSWORD: {password.strip()}')
    except FileNotFoundError:
        print('No passwords saved')

# main loop
while True:
    user_input = input('Select your option (v: view, a: add, q: quit): ')
    if user_input.lower() == 'v':
        print('Your passwords are as follows:')
        view_password()
    elif user_input.lower() == 'a':
        print('Let\'s add a new user password')
        user_name = input('Enter name: ')
        user_pass = input('Enter password: ')
        add_password(user_name, user_pass)
    elif user_input.lower() == 'q':
        break
    else:
        print('Invalid input!')
        continue
