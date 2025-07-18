#Anael Shahbaz
#Monday, June 16
#AnaelGame.py
#This program is a horror game, which asks for the user's command, in order to proceed. The only objective is>

#Start the game:
import random #Will need this for future usage

def UserName():
  player_name = input("Enter player's name: ") #player enters their name
  print("WELCOME", player_name,"TO ILLUSIONED CHOICE (game name).") #Welcome message
  rules = input("Would you like to read the rules? (yes/no): ")
  #If they say yes, it will print the rules. Otherwise it will just start the game.
  if rules == ("yes"):
    print("1. This is a one player choice game")
    print("2. You have an initial of 100 health")
    print("3. By choosing the wrong choice you can lose your health.")
    print("4. You will be given an option, to choose from left or right, yes or no, and numbered choices")
    print("5. Your goal is to leave the haunted house, unscathed")
    print("6. You can always play the game again, if you lose, but since the choices are randomized, you won't get the same choice")
  else: #If they say no, it will just print a blank line. and then start the game.
    print(" ")
  return player_name #Player's name is returned for future usage

#Before I initialize the game, I will introduce the lose and gain health function because that will be important for the function

Health = 100 #Health is a variable with a global scope, so we don't write that in the function  

def LoseHealth(): #Calling this function will reduce users health by 5
  global Health
  Health = Health - 5
  print("Your current Health is:", Health)
  return Health #This is really important, because we can then use the reduced value in future

def GainHealth():
  global Health
  Health = Health + 5
  print("Your current Health is:", Health)
  return Health 

#I'm going to make the initialize game function now, because we can now use the LoseHealth and GainHealth

def Initialize_Game(player_name):
#This is where I write the story, and where it all starts
  party_scene = input(player_name + " is formally invited to a high school party, would you like to go? ")
  if (party_scene == "no") or (party_scene == "No"):
    friend_scene = input("*NightTime: You're asleep, when suddenly you hear a creak coming from downstairs. Goosebumps rise on your arms, as you carefully thread down the stairs. THERE IS NO ONE HERE! But that wasn't for long, as you saw a shadow creep by. Curiousty got the better of you, and you walked towards the figure. Suddenly you hear* ""BOO"", *and you quickly recognize that voice, as your friends voice. You turn around to meet your friends face to face. They all start pleading you to go to the party. Your heart softens seeing them beg like this.* Do you go?")
    if (friend_scene == "no") or (friend_scene == "No"):
      print("Friend 1(Azazel): You're a coward, you're missing out on the best party of the year!")
      print("Friend 2(Nyx): Guess we have to take the more drastic measures")
      print("*There is a look of panic on your face, you know your friends can't be trusted*")
      print("Friend 3(Anubis): Azazel, did you bring, what I told you to?")
      print("Friend 1(Azazel): Yes, I did. Here it is. *Azazel hands Anubis a dark glass jar, and there seems to be a certain type of liquid in it*")
      print("*You try to run, but your friends are too fast, Nyx quickly grabs your arm, and Anubis pours the liquid onto a cloth, and wraps it around your mouth and nose*")
      print("*You try to scream, but the cloth is too tight, and you can't make a sound*")
      print("Chloroform....*The last thought exists your mind as you fall asleep*")
      print("...")
      print("...")
      print("...")
      print("You wake up, and you see your friends, it seems like your in front of a haunted house")
      LoseHealth()
    else:
      print("*You decide to go to the party, and you're friends look slightly disappointed*")
      print("*Friend 1(Azazel): You're a good friend, you're going to have a great time!*")
      print("Friend 3(Anubis: I wanted to use the drastic measure *muttered*")
      print("*Friend 2(Nyx) nudges Anubis, and Anubis looks away*")
      print("You're confused, but decide not to pester them")
      print("You are peer pressure to go to a haunted house with your friends")
  else:
    print("*You decide to go to the party*")
    print("~Good choice...saved yourself from a lot of trouble~")
    print("You are peer pressure to go to a haunted house with your friends")

#This function solely is for choices
def choice():
  choice = int(input("Which choice do you choose? (Choice 1/Choice 2/Choice 3):"))
  right_choice = random.randrange(1,4)
  if choice == right_choice:
    print("It is the right choice, unfortunatly you gain health")
    print("......")
    GainHealth()
    print("......")
  else:
    print("You could've made a better choice, fortunately you lose health")
    print("......")
    LoseHealth()
    print("......")
  return choice

def maze(): #This is the maze function, and it will be used at a certain point
  count = 0
  while count < 15:
    print("Choice 1: Left")
    print("Choice 2: Right")
    print("Choose number 1 or 2: ")
    choice = int(input("Which way do you want to go? (Left/Right):"))
    count = count + 1
    right_choice = random.randrange(1,3)
    count = count + 1
    if right_choice == choice:
      print("That is the right way! You gain health! I wish you chose wrong")
      print("......")
      GainHealth()
      
      print("......")
    else:
      print("That is the wrong way, GOOD JOB! Here come the zombies, and the spikes!")
      LoseHealth()
      
      
#This is the door stage, where the user will have to make a choice
def Door_Stage():
  print("You come across three doors, and you have to choose one of them.")
  print("If you don't choose the right door, you will lose health")
  print("Choice 1: Left Door")
  print("Choice 2: Middle Door")
  print("Choice 3: Right Door")
  print("Good luck choosing the right door, you'll need it")
  choice()
  print("You have to choose again, there are another triple doors waiting for you, hehehehehe")
  count = 1
  while count < 5:
    print("Choice 1: Left Door")
    print("Choice 2: Middle Door")
    print("Choice 3: Right Door")
    choice()
    count = count + 1
    print("You have to choose again, there are another triple doors waiting for you, hehehehehe")
  print("I'm just joking, there are no more doors...hehehe")

def Haunted_House(): #This is the beginning
  print("You are infront of a haunted house, and you have to get out")
  print("Choice 1 - Leaving the House")
  print("Choice 2 - Entering the House")
  print("Choice 3 - Exploring Leaving the House")
  choice1 = int(input("Do you want to leave the house, enter the house, or explore the house? (1/2/3):"))
  while choice1 == 1:
    print("Your friends are watching you, you can't leave. And even if they weren't there, the house wouldnt let you leave.")
    print("So choose again:")
    print("You are in a haunted house, and you have to get out")
    print("Choice 2 - Entering the House")
    print("Choice 3 - Exploring Leaving the House")
    choice1 = int(input("Do you want to leave the house, enter the house, or explore the house? (2/3):"))
    while choice1 == 2:
      print("It was too dark, you tripped and now your nose is bleeding, because you fell face first onto the stairs")
      LoseHealth()
      print("So choose again:")
      print("You are in a haunted house, and you have to get out")
      print("Choice 1 - Leaving the House")
      print("Choice 3 - Exploring Leaving the House")
      choice1 = int(input("Do you want to leave the house, enter the house, or explore the house? (1/3):"))
  while choice1 == 2:
    print("It was too dark, you tripped and now your nose is bleeding, because you fell face first onto the stairs")
    LoseHealth()
    print("So choose again:")
    print("You are in a haunted house, and you have to get out")
    print("Choice 1 - Leaving the House")
    print("Choice 3 - Exploring Leaving the House")
    choice1 = int(input("Do you want to leave the house, enter the house, or explore the house? (1/3):"))
    while choice1 == 1:
      print("Your friends are watching you, you can't leave. And even if they weren't there, the house wouldnt let you leave.")
      print("So choose again:")
      print("You are in a haunted house, and you have to get out")
      print("Choice 2 - Entering the House")
      print("Choice 3 - Exploring Leaving the House")
      choice1 = int(input("Do you want to leave the house, enter the house, or explore the house? (2/3):"))
  if choice1 == 3:
    print("You explore around the house")
    print("You find a dead body, fear engulfs you, fogging your mind")
    print("Gulping, you search the body and find a yello flashligh")
    print("Using the flashlight, you see the stairs and don't trip, carefully entering the house.")

Day = 1
def progress(): #This is for the progress
  global Day
  Day = Day + 1
  print("Day:", Day)
  return Day

def EndGame(): #This is the ending
  print("You come out of the house, finally, the crisp sun rise waiting in patience for you")
  print("Thoughts run through your mind, however your mind was blank at the same time")
  print("You think to yourself, if this was all a reality? a nightmare? or a prank?")
  print("One last choice to make:")
  print("Choice 1: Reality")
  print("Choice 2: Nightmare")
  print("Choice 3: Prank")
  choice2 = int(input("What do you think it was? (1/2/3):"))
  if choice2 == 1:
    print("""IT WAS A PRANK!!!""")
    print("You hear someone yell that")
    print("You turn around and see your friends laughing")
    print("They are all alive, and your eyes widen from shock")
    print("Your face is red from anger, as you walk away")
    print("Your friends walk after you, laughing and apologizing")
    print("Your Health is:back at a 100!")
  elif choice2 == 2:
    print("It was reality....")
    print("Your friends are all dead, and you're alone")
    print("And what? you thought you made it out?, no")
    print("You're stops halluciting, as you see the reality in front of you")
    print("You see that you are still in the haunted house...stuck")
    print("forever...the house has taken a liking on you")
    print("Your health is slowly going down")
    print("You dont even panic, because you know, you're already dead, you have been dead since you got the invite")
    print("Death slowly succumbs you, throwing up your organs and skeleton")
    print("You see a person walking towards your body, and they look oddly like you, the same eyes, and the same nose, they have fear written all over their face, they gulp and start searching your body, finding a yellow flashlight, oddly similar to the one you found....")
    print("You see them turn around, and you see them laughing, and you see them laughing, and you see them laughing, and you see them laughing, and you see them laughing, and you see them laughing, and you see them laughing")
    print("Everything darkens...")
  else:
    print("It was a nightmare....")
    print("You wake up, and you see your friends, all alive and well")
    print("Everything is normal, as you go to school")
    print("Your english teacher introduces you to a new book, called Illusioned Choice")
    print("You read it, and you see the same story, and you see the same choices, and you see the same ending")
    print("Was it really all a dream?...")

def MainGame(): #This is the main game function, where the main game is played
  player_name = UserName()
  Initialize_Game(player_name)
  Haunted_House()
  print("Your friends trail behind you, entering the house with you")
  print("You can hear creaking sounds, and small voices laughing and crying for help")
  print("An eerie feeling engulfs your stomach")
  leave = input("Do you want to ask your friends to leave the house? (yes/no):")
  if leave == "yes":
    print("They laugh at you, pushing you to walk forward")
  else:
    print("The eerie feeling is still there")
  print("After walking, you come across a door")
  print("Your friends push you to choose a door.")
  Door_Stage()
  print("The door closes before Anubis (friend 3), can enter")
  print("You hear a blood curling scream, that sounds awfully similar to your friends voice")
  print("You have to keep going, your friends coax you to move forward")
  print("You were so distracted, that you didnt notice the glass, and you stepped on it")
  LoseHealth()
  print("You can't walk properly, because you're bleeding")
  print("You need a whole day to recover")
  progress()
  print("You finally recover, and you're ready to go")
  print("You walk up the stairs, and find a entrance")
  print("You walk through the entrance, and you find yourself in a maze")
  print("You have to find your way out")
  maze()
  print("You finally find your way out, and you see a door")
  print("You walk through the door, and you see a staircase")
  print("You see a room, that looks like a kitchen")
  print("On the dining table you see three shiny red apples")
  print("Your stomach rumbles, as if it saw the apples too")
  print("You find a note above the apples")
  print("~2 Apples Are Poisonous~")
  print("Your other two friends make you choose first")
  print("Choice 1: Apple 1")
  print("Choice 2: Apple 2")
  print("Choice 3: Apple 3")
  choice()
  print("Even if you ate the poisonous apple, you dont die, your other two friends die in front of your eyes")
  print("Arrows piercing their bodies")
  print("You sprint out of the house, and run through the door that says EXIT, scared for your life")
  EndGame()
  
def Play_again(): #This function actually plays the game, and asks if the user wants to play again? 
  MainGame()
  play_again = input("Do you want to play again? (yes/no):")
  while play_again == "yes":
    MainGame()
    play_again = input("Do you want to play again? (yes/no):")
Play_again()
#The Game ends here  