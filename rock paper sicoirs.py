import random
mylist = ["rock", "paper", "scissors"]
CPU = random.choice(mylist)


print ("ARe you ready to play rock, paper, scissors? ")
print ("Please select an otpion when you are ready to play: ")
print ("1 Rock")
print ("2 paper") 
print ("3 scissors")                                                                 

player = input ("choose from 1-3:")
if player == CPU:
    print ("tie")
elif player == 1:
    if CPU == 2:
        print ("You Lose")
    else:
        print ("YOU WIN")
elif player == 2:
    if CPU == 1:
        print ("YOU WIN")
    else:
        print ("You Lose")    
elif player == 3:
    if CPU ==2:
        print ("YOU WIN")
    else:
        print ("You lose")
print ("Thanks for playing a game of Rock, Paper, Scissors")
    
