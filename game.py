import random
for i in range(20):

    my_input= input("chose :rock, paper , or scissors : ")

    if my_input == "rock" or my_input == "paper" or my_input == "scissors":
        options = ['rock', 'paper', 'scissors']
        computer_choice = (random.choice(options))
        print ("computer chocie " + computer_choice)

        if my_input == "rock" and computer_choice ==  "scissors":
            print ("you win")

        elif my_input == "paper" and computer_choice == "rock":
            print("you win") 

        elif my_input == "scissors" and computer_choice == "paper":
            print("you win") 

        elif computer_choice == "rock" and my_input == "scissors":
            print ("computer win")

        elif computer_choice == "paper" and my_input == "rock":
            print ("computer win")

        elif computer_choice == "scissors" and my_input == "paper":
            print ("computer win")

        elif computer_choice == "paper" and my_input == "paper":
            print ("no one win")

        elif computer_choice == "rock" and my_input == "rock":
            print ("no one win")

        elif computer_choice == "scissors" and my_input == "scissors":
            print ("no one win")
    else:
        print ("enter a vilade text")
        
