
correct_number = 8
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    secret_number = int(input("enter a number between 1 to 10: "))
    guess_count += 1
    if secret_number == correct_number:
        print("YAY YOU WON!!!!!!!!!")
        break
    else:
        if secret_number in range(1, 6):
            print("to low, try again")
        elif secret_number in range(6, 7):
            print("low and too close, try again")
        elif secret_number in range(9, 11):
            print("High and too close, try again")
else:
    print("SORRY BETTER LUCK NEXT TIME")



