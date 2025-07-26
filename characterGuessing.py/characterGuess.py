import random

names = ['Rahimi', 'Akbari', 'Amiri', 'Hussaini', 'Mohammadi', 'Ahmadi', 'Sultani']
select_name = random.choice(names).lower()
guess_list = ['-'] * len(select_name)
current_guess = " ".join(guess_list)
guess_count = len(select_name)

while guess_count > 0:
    try:
        guess_char = input('Enter your char: ')
        if guess_char in select_name:
            if guess_char in guess_list:
                print('you guess this character before.\nguess the new character.')
            else:
                for i, char in enumerate(select_name):
                    if char == guess_char:
                        guess_list[i] = guess_char
                current_guess = " ".join(guess_list)
                print(f'perfect -> {current_guess}')
                if '-' not in guess_list:
                    print('you win!')
                    break
        else:
            guess_count -= 1
            print(f'wrong! -> remaind guess {guess_count}')
    except:
        print("invalid input!")