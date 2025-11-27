import random

def play():
    print("=== Rock, Paper, Scissors ===")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()
        
        if user == "q":
            print("Thanks for playing!")
            break
        if user not in choices:
            print("Invalid choice, try again.")
            continue
        
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")
        
        if user == computer:
            print("It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play()
