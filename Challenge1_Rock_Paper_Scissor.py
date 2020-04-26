"""The Rock, Paper, Scissors Game"""
# This program prompts a user to play a game of rock, paper, scissors against a computer. 

import random

game = {"rock": {"paper":"You lose!",            #nested dictionary of all possible outcomes
                 "scissors":"You win!"},
        "paper": {"rock":"You win!",
                  "scissors":"You lose!"},
        "scissors": {"rock":"You lose!",
                     "paper":"You win!"},
        }

#user first prompt - if they want to play go through while loop, else print a 'goodbye' statement
player_active = input("Hi! Would you like to play Rock, Paper, Scissors? (y/n) ")
done_game = "Maybe next time :)"

game_active = True                  #while loop flag
while game_active:                      #while loop to allow user to play again
    if player_active.lower() == 'n':            #if user 'says no' to playing, break out of while loop
        print(done_game)
        break
    else:                                       #else, prompt user to see rules or not
        rules = input("\nDo you need to see the rules? (y/n) ")
        if rules.lower()  == 'n':                   #if user 'says no' to rules, print 'start game' statement to get user ready
            print("\nOkay, let's play!")
        else: 
            print("\nThe rules for Rock, Paper, Scissors are: ")           #print the rules of the game if prompted
            print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")


    ready = input("\nAre you ready? (type 'n' to quit) (y/n) ")    #get user ready before game starts
    if ready.lower() == 'n':                    #if player isn't ready, break out of while loop
        print(done_game)
        break 
    else:
        player_choice = input("Rock, Paper, Scissors, Go! (input your choice): ")   #if player ready prompt user choice
        player_choice = player_choice.lower()

    comp_choice = random.choice(list(game.keys()))      #randomize the computer's choice

    if player_choice == comp_choice:           #if user's choice equals computer's random choice, print it's a draw
        print(f"It's a draw!")

    elif player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":                      #if player isn't ready then player_choice = 'done', print 'goodbye' statement
        print(f"\nI'm sorry, that's not an option.")

    else:
        result = game[player_choice][comp_choice]           #if user choice doesn't equal computer choice print the comp choice and the result
        print(f"\nThe computer chose {comp_choice}. {result}.")

    play_again = input("\nWould you like to play again? (y/n) ")    #prompt user to play again 
    if play_again == 'y':
        continue                                    #if user wants to play again, go back to beginning of while loop
    else:
        print("Thanks for playing!")                #if user doesn't want to play again, print 'good bye and thanks' statement and exit while loop
        game_active = Falsey
        




'''If the user wins, then display "You win!" If they lose against the computer, then display "You lose." If the computer and the user have 
the same play choice, display "It's a draw."  
BONUS: Randomize the play choice for the computer (hint: Python has a library called random). Also ask the user if they would like to 
play again. If they do, start the game again but if not, thank the user for playing the game.'''