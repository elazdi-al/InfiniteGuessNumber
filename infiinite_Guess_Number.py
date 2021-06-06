import random

choice = int(input(
    "Hey, would you like the computer to choose a number or do you want to do so? (press 1 for the first choice and 2 for the second one"))
# first game :
if choice == 1:
    print("The computer chose a number, try to guess it")

    def guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input("Your guess: "))
            if guess < random_number:
                print("Too low, try again")
            elif guess > random_number:
                print("Too high, try again")

        print(f"Yayyy, you found the right number: {random_number}")

    guess(10)

# second game :
elif choice == 2:
    print("Think of a number, the computer is going to try to guess it")

    def guess_2(x):
        low = 1
        high = x
        guess = random.randint(low, high)
        feedback = input(
            f"Is {guess} the correct number ? (answer using Y for correct, H for too high, and L for too low).")
        while feedback != "Y":
            if feedback == "H":
                high = guess - 1
                guess = random.randint(low, high)
            if feedback == "L":
                low = guess + 1
                guess = random.randint(low, high)
            feedback = input(
                f"Is {guess} the correct number ? (answer using Y for correct, H for too high, and L for too low).")

    guess_2(10)
    print("Yayyy, the computer guessed the right number")

print("Thanks for playing my game ;)")
