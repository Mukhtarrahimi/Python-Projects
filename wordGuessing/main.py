import random
names = ["Rahimi", "Akbari", "Hussaini", "Mohammadi", "Ahmadi",
         "Mandegar", "Hassani", "Jafari","Qasimi", "Alizada",
         "Amiri", "Nazari", "Rezaie", "Hashimi", "Rasuli", "Rahmani"]

select_name = random.choice(names).lower()
guess_list = [' - ']* len(select_name)
current_guess = " ".join(select_name)
guess_count = len(select_name)


