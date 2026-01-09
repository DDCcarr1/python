# Imports
import random as rand
import time as t

# Main game function
def play():
    # Check for AI
    useai = input("Do you want to play against AI? (y/n): ")

    # Validate input
    while useai not in ["y", "n"]:
        useai = input("Please enter either y or n.\nDo you want to play against AI? (y/n): ")

    # Get player names
    p1_name = str(input("\nEnter Player 1's name: "))

    # Default name if blank
    if p1_name.strip() == "":
        p1_name = "Player 1"

    # Get Player 2's name if not playing against AI
    if useai == "n":
        p2_name = str(input("Enter Player 2's name: "))
        
        # Default name if blank
        if p2_name.strip() == "":
            p2_name = "Player 2"

    # Add blank line for spacing
    print()

    # Get Player 1's input
    p1_input = str(input(p1_name + ": Rock (r), Paper (p), Scissors (s): "))

    # Validate input
    while p1_input not in ["r", "p", "s"]:
        p1_input = str(input("Please enter either r, p, or s.\n" + p1_name + ": Rock (r), Paper (p), Scissors (s): "))
        
    # Convert input to full word
    p1_full = ""
    if p1_input == "r":
        p1_full = "Rock"
    elif p1_input == "p":
        p1_full = "Paper"
    else:
        p1_full = "Scissors"

    # Clear screen simulation
    if useai == "n":
        for i in range(50):
            print()
            
        # Say Player 1 has made their choice
        print(p1_name + " has made their choice.")
        
        # Get Player 2's input
        p2_input = str(input(p2_name + ": Rock (r), Paper (p), Scissors (s): "))
        
        # Validate input
        while p2_input not in ["r", "p", "s"]:
            p2_input = str(input("Please enter either r, p, or s.\n" + p2_name + ": Rock (r), Paper (p), Scissors (s): "))
            
        # Convert input to full word
        p2_full = ""
        if p2_input == "r":
            p2_full = "Rock"
        elif p2_input == "p":
            p2_full = "Paper"
        else:
            p2_full = "Scissors"
            
        # Clear screen simulation
        for i in range(50):
            print()
            
        # Say Player 2 has made their choice
        print(p2_name + " has made their choice.")
        
    # Player vs AI mode
    if useai == "y":
        # Get AI input
        aiinput = rand.choice(["Rock", "Paper", "Scissors"])
        aifull = aiinput

        # Show choices with delays
        print()
        t.sleep(0.5)
        print(p1_name + " chose " + p1_full)
        t.sleep(0.5)
        print("AI chose " + aifull)
        t.sleep(0.5)
        print()
        
        # Determine winner
        if (p1_full == "Rock" and aifull == "Scissors") or (p1_full == "Paper" and aifull == "Rock") or (p1_full == "Scissors" and aifull == "Paper"):
            # Player 1 wins condition
            print(p1_name + " wins!")
            
        # Tie condition
        elif p1_full == aifull:
            print("It's a tie!")
            
        # AI wins condition
        else:
            print("AI wins!")
            
    # Player vs Player mode
    else:
        # Show choices with delays
        print()
        t.sleep(0.5)
        print(p1_name + " chose " + p1_full)
        t.sleep(0.5)
        print(p2_name + " chose " + p2_full)
        t.sleep(0.5)
        print()

        # Determine winner
        if (p1_full == "Rock" and p2_full == "Scissors") or (p1_full == "Paper" and p2_full == "Rock") or (p1_full == "Scissors" and p2_full == "Paper"):
            # Player 1 wins condition
            print(p1_name + " wins!")
            
        # Tie condition
        elif p1_full == p2_full:
            print("It's a tie!")
            
        # Player 2 wins condition
        else:
            print(p2_name + " wins!")

    # Add spacing and delay before replay prompt
    print()
    t.sleep(0.5)

    # Replay prompt
    replay = ""
    replay = input("Would you like to play again? (y/n): ")

    # Validate input
    while replay not in ["y", "n"]:
        replay = input("Please enter either y or n.\nWould you like to play again? (y/n): ")
        
    # Replay condition
    if replay == "y":
        # Clear screen simulation
        for i in range(50):
            print()
        
        # Print quick message
        print("Starting a new game...\n")
        t.sleep(1)
        
        # Restart game
        play()

    # Exit message
    else:
        print("\nThanks for playing Rock, Paper, Scissors!")
        
# Start the game
play()