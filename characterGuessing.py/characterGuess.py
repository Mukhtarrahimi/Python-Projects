import random

names = ['Rahimi', 'Akbari', 'Amiri', 'Hussaini', 'Mohammadi', 'Ahmadi', 'Sultani']
select_name = random.choice(names).lower()
guess_list = ['-'] * len(select_name)
current_guess = " ".join(guess_list)
guess_count = len(select_name)