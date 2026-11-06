pass_rate = 0
common_advice = 0
length_advice = 0
special_advice = 0
capital_advice = 0

while True:
    password = input("Enter a password: ")

    badpasswords= ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    injections= ['1=1', 'injection' , 'badcode'  ]

    if password in injections:
        print("this password is dangerous please enter a diffrent one")
    else:
        pass_rate += 20
        break


if password in badpasswords:
    common_advice += 1
else:
    pass_rate += 20

leanth = len(password)

if leanth < 12:
    length_advice = 1
else:
    pass_rate += 20

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
if any(char in special_characters for char in password):
     pass_rate += 20
else:
    special_advice += 1

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
if any(char in capital_letters for char in password):
    pass_rate += 20
else:
    
    capital_advice += 1

print("your password is rated at", pass_rate, "%")

if pass_rate == 100:
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

if common_advice == 1:
    print("Your password is too common. Please choose a different password.")
if length_advice == 1:
    print("Your password is too short. Please choose a different password.")
if special_advice == 1:
    print("Your password does not contain enough special characters. Please choose a different password.")
if capital_advice == 1:
    print("Your password does not contain enough capital letters. Please choose a different password.")