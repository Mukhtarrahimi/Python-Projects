while True:
    user_input = ("Select your option (v: view, a: add, q: quit)")
    if user_input.lower() == "v":
        print("your password are as follow:")
        pass
    elif user_input.lower() == "a":
        print("let's add a new user_password")
    elif user_input.lower() == "q":
        break
    else:
        print("invalid input!")
        continue