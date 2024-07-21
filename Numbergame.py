import random
def play_game():
    print("May I ask you for your name?")
    name = input()
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200")
    print("Go ahead. Guess!")
    
    n = random.randint(1, 200)
    for i in range(0, 5):
        x = int(input("Guess: "))
        if n > x:
            print("The number that you have entered is too low")
        elif n < x:
            print("The number fthat you have that is too high")
        else:
            print(f"Yes. The number I was thinking of was {n}")
            break
    else:
        print(f"Nope. The number I was thinking of was {n}")
    
    print("Do you want to play again?")
    play_again = input()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing!")

play_game()
