import random
#rock,papaer,scssiors
#play : player aginst computer
while True :
    choises = ["rock","paper","scssiors"]
    computer = random.choice(choises)
    player =None
    while player not in choises:
        #
        player =input("rock, paper,or scssiors:").lower()
        if player == computer:
           print("player is :", player)
           print("computer is :", computer)
           print("yeee")
        elif player == "rock": #>>>>>>>1
         if computer == "paper":
           print("player is :", player)
           print("computer is :", computer)
           print("you are loser")
         elif player == "paper":
          if computer == "rock": #>>> 2
             print("player is :", player)
             print("computer is :", computer)
             print("you are winner")
          elif player == "rock": #>>>>>>>3
           if computer == "scssiors":
             print("player is :", player)
             print("computer is :", computer)
             print("you are winner")
          elif player == "scssiors":#>>>>>>>>>4
           if computer == "rock":
             print("player is :", player)
             print("computer is :", computer)
             print("you are loser")
          elif player == "paper":#>>>>>>>>>5
           if computer == "scssiors":
             print("player is :", player)
             print("computer is :", computer)
             print("you are loser")
         elif player == "scssiors":#>>>>>>>>>>>6
          if computer == "paper":
            print("player is :", player)
            print("computer is :", computer)
            print("you are winner")
    play_agine = input("do you like play agine? (yes,no)")
    if play_agine != "yes":
        break
print("bye")
