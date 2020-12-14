import win32com.client as wincl
from pygame import mixer
speak=wincl.Dispatch("SAPI.spVoice")
import random
import time
from random import choice 
from time   import sleep
import webbrowser


def rock_paper():
        player_points=0
        computer_points=0
        out_of_cards=False
        max_no_of_turns=5
        no_of_turns=0

        name=input("\033[1;32m [+] Enter your name here: \033[1;m")
        print()
        time.sleep(.9)
        print("\033[1;32m [+] Welcome to the game, \033[1;m" +name+ "!")
        print()
        time.sleep(1.3)
        print("How to play: ")
        time.sleep(1.2)
        print("1.You can only use the cards that you have.")
        time.sleep(2)
        print("2.Everytime the result is draw, you will\n  get card.")
        time.sleep(2)
        print("3.The first player who got highest score after\n  5 turns will win the game.")
        time.sleep(2)
        print("4.If you enjoy the game don't FORGET to\n  click the star button.")
        print()
        time.sleep(2)

        print("\033[1;32m [+] Game loading...10% \033[1;m")
        time.sleep(1.2)
        print("\033[1;32m [+] Game loading...29% \033[1;m")
        time.sleep(1.5)
        print("\033[1;32m [+] Game loading...48% \033[1;m")
        time.sleep(2)
        print("\033[1;32m [+] Game loading...69%\033[1;m")
        time.sleep(1)
        print("\033[1;32m [+] Game loading...88%\033[1;m")
        time.sleep(1)
        print("\033[1;32m [+] Game loading...99%\033[1;m")
        time.sleep(2)
        print("\033[1;32m [+] Game loading...100%\033[1;m")
        time.sleep(.7)
        print ()
        print("Game Started")
        time.sleep(.3)
        print()
        print("Player points: " +str(player_points))
        print("Computer points: " +str(computer_points))
        print()
        card=["rock","paper","scissor","rock","paper","scissor"]
        player_card=random.sample(card,k=5)
        computer_card=random.choices(card,k=5)

        print()
        while no_of_turns != max_no_of_turns:
            time.sleep(1.3)
            print("Your card: ")
            print(str(player_card))
            print()
            player_attack=input("\033[1;34m Enter your attack here: \033[1;m")
            print()
            time.sleep(1)
            print("\033[1;32m You used: \033[1;m")
            print(player_attack)
            time.sleep(1)
            computer_attack=random.choice(computer_card)
            print()
            print("\033[1;32m Computer used: \033[1;m")
            print (computer_attack)
            time.sleep(1)

            if player_attack=="paper" and computer_attack=="rock":
              try:
                print()
                time.sleep(1)
                print("You earn 1 point, you win!!")
                print()
                player_points+=1
                player_card.remove(player_attack)
                time.sleep(1.5)
                print("Your score: " + str(player_points))
                print("Computer score: " + str(computer_points))
                no_of_turns+=1
                print()
              except:
                time.sleep(1.3)
                print("Attack doesn't exist on your card")
                print()
         
            elif player_attack=="rock" and computer_attack=="paper":
              try:
                print()
                computer_points+=1
                player_card.remove(player_attack)
                time.sleep(1)
                print("Computer earn 1 point, computer win!!")
                print()
                time.sleep(1.5)
                print("\033[1;31m Your score: \033[1;m" + str(player_points))
                print("\033[1;31m Computer score: \033[1;m" + str(computer_points))
                no_of_turns+=1
                print()
              except:
                time.sleep(1.3)
                print("Attack doesn't exist on your card")
                print()
            elif player_attack=="scissor" and computer_attack=="paper":
              try:
                print()
                time.sleep(1)
                print("You earn 1 point, you win!!")
                print()
                player_points+=1
                player_card.remove(player_attack)
                time.sleep(1.5)
                print("\033[1;31m Your score: \033[1;m" + str(player_points))
                print("\033[1;31m Computer score: \033[1;m " + str(computer_points))
                no_of_turns+=1
                print()
              except:
                time.sleep(1.3)
                print("Attack doesn't exist on your card")
                print()
            elif player_attack=="paper" and computer_attack=="scissor":
              try:
                print()
                time.sleep(1)
                print("Computer earn 1 point, computer win!!")
                print()
                computer_points+=1
                player_card.remove(player_attack)
                time.sleep(1.5)
                print("\033[1;31m Your score: \033[1;m" + str(player_points))
                print("\033[1;31m Computer score: \033[1;m" + str(computer_points))
                no_of_turns+=1
                print()
              except:
                time.sleep(1.3)
                print("Attack doesn't exist on your card")
                print()
            elif player_attack=="scissor" and computer_attack=="rock":
              try:
                time.sleep(1)
                print()
                print("Computer earn 1 point, computer win!!")
                print()
                computer_points+=1
                player_card.remove(player_attack)
                time.sleep(1.5)
                print("\033[1;31m Your score: \033[1;m" + str(player_points))
                print("\033[1;31m Computer score: \033[1;m" + str(computer_points))
                no_of_turns+=1
                print()
              except:
                time.sleep(1.3)
                print("Attack doesn't exist on your card")
                print()
            elif player_attack=="rock" and computer_attack=="scissor":
              try:
                print()
                player_points+=1
                player_card.remove(player_attack)
                time.sleep(1)
                print("You earn 1 point, you win!!")
                print()
                time.sleep(1.5)
                print("\033[1;31m Your score: \033[1;m" + str(player_points))
                print("\033[1;31m Computer score: \033[1;m" + str(computer_points))
                no_of_turns+=1
                print()
              except:
                time.sleep(1.3)
                print("Attack doesn't exist on your card")
                print()
   
            elif player_attack==computer_attack:
              try:
                print()
                time.sleep(1.3)
                print("It is draw")
                time.sleep(1)
                print()
                print("You draw 1 card")
                player_card=player_card+random.sample(card, k=1)
                print()
              except:
                print("You don't have this card")
    
            else:
              print()
              time.sleep(1.3)
              print("invalid attack")
              print()                              
  
    
        if player_points>computer_points:
          time.sleep(.9)
          print()
          print("\033[1;32m Congatulations!, you win!\033[1;m")
          scores += 10
          print("\033[1;33m [+] Stones : \033[1;m "+ Stons )
          print("\033[1;33m [+] Scores : \033[1;m "+ scores )
          time.sleep(1)
          print("Thank you")
          time.sleep(3)
          cigar()
        elif player_points<computer_points:
          time.sleep(.9)
          print()
          print("\033[1;32m Computer win!\033[1;m")
          time.sleep(1)
          scores -= 5
          print("\033[1;33m [+] Scores : \033[1;m "+ scores )
          print("\033[1;33m [+] Stones : \033[1;m "+ Stons )
          print("Try again to play to win! next time ")
          time.sleep(3)
          tadpole()
          print("Thank you!")




def earth_chat():
        # I imported time so that user can read it 
        print("Hi! 😃😃")
        input("your response: ")
        print("My name is scot")
        time.sleep(1)
        name = "scot: What is  your name"
        print(name)
        x=input()
        time.sleep(1) 
        print("scot: "+ x+" is a very cool name🤘🤘🤘")
        # if your age is greater than 30 it would say young else old in a funny way
        time.sleep(2)
        y=int(input("scot: What is your age "+ x+" :"))
        if y<30:
           print("scot: Oh you are so young "+ x+"🔥🔥🔥")
        else:
           y>30
           print("scot: Oh my god! your\nyoungness has gone🤣🤣🤣🤣,\nsorry sorry I was just joking ")
           time.sleep(3)
        z=input("scot: hey "+x+" where do you live ")
        print("scot: wow \n"+ z+" is a amazing place I will visit it soon\n through google map🤣🤣🤣. ")
        time.sleep(3)
        a=input("scot: Who is your favourite \ncharacter in marvel (Spiderman🕷️🕸️ or Ironman🧠)")
        s=a.lower()
# there are two different reply for spiderman and ironman and by chance if didnot typed bith of them the output will be different
        if s=="spiderman":
           print("scot: Good choice but I like\n ironman(the intelligent one)")
        elif s=="ironman":
           print("scot: Great choice👌👌👌")
        else:
           print("scot: Let's leave this question😅😅")
        time.sleep(2)
        print("scot: Well I have got all your information 😼😼\nIf you dont want your privacy to be leaked \ngive me a star 🌟 ")
        time.sleep(2)
        input(" your response to this betrayal:")
        print("scot: I assume you abused me🤔🤔🤔")
        time.sleep(2)
        print("scot: you are a boring person "+x+"😩😩😵😵 \n go Away !! ")
        print("\033[1;32m [+] "+ user_ID +" your keep redirecting in space know beausce you have the space stone \033[1;m ")
        pin_wheel()


def game():
        nome = input("What is your name?\n>>>")
        pacote = ["demonic eye","goblin","slime","zombie","spider","skeleton"]

        monstroescolhido = random.choice(pacote)

        print(" ")
        print("an {} appeared!".format(monstroescolhido))
        print(" ")
        jogador = 100
        monstro = 100

#Your attack

        while jogador > 1:
          time.sleep(1)
          print("==================")
          print(" ")
          print("{}'s life: {}\n{}'s life: {}".format(nome, jogador, monstroescolhido, monstro))
          print(" ")
          time.sleep(1)
          print("What {} will do?".format(nome))
          ataque = int(input("[1] Normal attack\n[2] Special attack\n[3] Recover life\n>>>"))
          print(" ")
  
          if ataque == 1:
            time.sleep(1)
            print("{} dealt 15 damage!".format(nome))
            monstro = monstro - 15
            time.sleep(1)
            print("{} have {} life now!".format(monstroescolhido, monstro))
            print(" ")
    
          elif ataque == 2:
            time.sleep(1)
            chance = random.randint(1,2)
    
            if chance == 1:
              print("{} dealt 35 damage!".format(nome))
              monstro = monstro - 35
              time.sleep(1)
              print("{} have {} life now!".format(monstroescolhido, monstro))
              print(" ")
      
            else:
              print("{} failed!".format(nome))
      
          elif ataque == 3:
            time.sleep(1)
            print("{} recovered 30 life!".format(nome))
            time.sleep(1)
            jogador = jogador + 30
            print("{} have {} life now!".format(nome, jogador))
    
    #Win or lose
    
          if jogador < 1:
            time.sleep(1)
            print("{} lose...".format(nome))
            print("lose.....................")
            time.sleep(2)
            break
    
          elif monstro < 1:
            time.sleep(1)
            print("{} wins!!".format(nome))
            print("wins....................")
            time.sleep(2)
            break
    
    #enemy attack
  
          print("==================")
          print(" ")
          print("{} time!".format(monstroescolhido))
          time.sleep(2)
          print(" ")
  
          ataqueinimigo = random.randint(1,3)
  
          if ataqueinimigo == 1:
            print("{} dealt 10 damage!".format(monstroescolhido))
            jogador = jogador - 10
            time.sleep(1)
            print("{} have {} life now!".format(nome, jogador))
            print(" ")
  
          elif ataqueinimigo == 2:
            print("{} dealt 15 damage!".format(monstroescolhido))
            jogador = jogador - 15
            time.sleep(1)
            print("{} have {} life now!".format(nome, jogador))
            print(" ")

          elif ataqueinimigo == 3:
            print("{} dealt 20 damage!".format(monstroescolhido))
            jogador = jogador - 20
            time.sleep(1)
            print("{} have {} life now!".format(nome, jogador))
            print(" ")
    
          print(" ")
  
  #win or lose 2
  
          if jogador < 1:
            time.sleep(1)
            print("{} lose...".format(nome))
            scores = scores - 5
            print("\033[1;32m [+] your points " + user_ID +".\033[1;m " + str(scores))
            time.sleep(2)
            stage_1()
    
          elif monstro < 1:
            time.sleep(1)
            print("{} wins!!".format(nome))
            scores = scores + 10
            print("\033[1;32m [+] your points " + user_ID +".\033[1;m " + str(scores))
            time.sleep(2)
            whirlpool()

def titon():
        print("""""""""\033[1;35m
                                              
                                                ___________.__   __                   
                                                \__    ___/|__|_/  |_   ____    ____  
                                                  |    |   |  |\   __\ /  _ \  /    \ 
                                                  |    |   |  | |  |  (  <_> )|   |  \.
                                                  |____|   |__| |__|   \____/ |___|  /
                                                                                   \/ 
                         ---------------------------------------------------------------------------------------
        
                                                                                       \033[1;m""""""""")
        
        time.sleep(2)
        print("\033[1;32m [+] wellcome to Titon " + user_ID +".\033[1;m ")                                                                               

def stage_1():
    secret_word="tixe"
    guess = ""
    guess_count = 0
    guess_limit = 6
    out_of_guess = False 

    print(" story ")

    while guess != secret_word and not( out_of_guess):
        if guess_count < guess_limit:
            guess = input("\033[1;32m [+] A:~ \033[1;m")
            guess_count += 1
        else:
            out_of_guess = True

    print("\033[1;m [+] ------------------------------------ ho ho that's amazing you find it -------------------------------\033[1;m")
    if out_of_guess:
        print("""\033[1;31m [+]------------------------------------ Hey i think you are stack ------------------------------------------ 
                                                                    [     Hint : MIRROR     ]
                                                                                                             \033[1;m""")
        s_word = "tixe"
        g_word  = ""
        while g_word != s_word :
            g_word = input("\033[1;32m [+] A:~ \033[1;m")
            
        print("\033[1;34m [+] ----------------------------------- hhhh0000 Bro you got it -------------------------------------------\033[1;m")
       
        

def music():
       mixer.init()

       mixer.music.load(r"C:\Users\bjman\OneDrive\Desktop\codes\theme.mp3")
       mixer.music.set_volume(10)
       mixer.music.play()
 

def whirlpool():
        print("""""""""\033[1;35m 
                                         _      ____   _     __               __
                                        | | /| / / /  (_)___/ /__  ___  ___  / /
                                        | |/ |/ / _ \/ / __/ / _ \/ _ \/ _ \/ / 
                                        |__/|__/_//_/_/_/ /_/ .__/\___/\___/_/  
                                                           /_/                  
                         ---------------------------------------------------------------
                                                                                       \033[1;m""""""""")
        
        time.sleep(2)
        print("\033[1;32m [+] wellcome to whirlpool " + user_ID +".\033[1;m ")
        print("\033[1;34m [+] I'm captain Marvel here to guide you \033[1;m")
        speak.speak("Wellcome to whirlpool " + user_ID)



def casio():
        print("""""""""\033[1;35m
                                              
                                     
                                                  _____         _    
                                                 / ___/__ ____ (_)__ 
                                                / /__/ _ `(_-</ / _ \_
                                                \___/\_,_/___/_/\___/
                         ---------------------------------------------------------------
                                                                                       \033[1;m""""""""")

        time.sleep(2)
        print("\033[1;32m [+] wellcome to Casio " + user_ID +".\033[1;m ")
        print("\033[1;34m [+]  I'm captain America here to guide you \033[1;m")
        speak.speak("Wellcome to Casio " + user_ID)


def pin_wheel():
        print("""""""""\033[1;35m
                                              
                                           ___  _        _      ____           __
                                          / _ \(_)__    | | /| / / /  ___ ___ / /
                                         / ___/ / _ \   | |/ |/ / _ \/ -_) -_) / 
                                        /_/  /_/_//_/   |__/|__/_//_/\__/\__/_/  
                         ---------------------------------------------------------------
                                                                                       \033[1;m""""""""")
        time.sleep(2)
        print("\033[1;32m [+] wellcome to Pin wheel " + user_ID +".\033[1;m ")
        time.sleep(1)
        print("\033[1;32m [+] I'm Tony strak\033[1;m ")
        time.sleep(1)
        print("\033[1;32m [+] here you have one task to move next step \033[1;m ")
        print("\033[1;31m [+] Here you Go........\033[1;m ")
        time.sleep(2)
        tic_toc_to()
        speak.speak("Wellcome to pin wheel " + user_ID)



def andromeda():
        print("""""""""\033[1;35m
                                              
                                   ___           __                      __    
                                  / _ | ___  ___/ /______  __ _  ___ ___/ /__ _
                                 / __ |/ _ \/ _  / __/ _ \/  ' \/ -_) _  / _ `/
                                /_/ |_/_//_/\_,_/_/  \___/_/_/_/\__/\_,_/\_,_/ 
                         ---------------------------------------------------------------
                                                                                       \033[1;m""""""""")
        time.sleep(2)
        print("\033[1;32m [+] wellcome to Andromeda " + user_ID +".\033[1;m ")
        print("\033[1;32m [+] I'm Dr. strange here yo have one small game to play & you get points too \033[1;m ")
        time.sleep(4)
        game()
        speak.speak("Wellcome to Andromeda" + user_ID)



def tadpole():
        print("""""""""\033[1;35m
                                          ______        __          __   
                                         /_  __/__ ____/ /__  ___  / /__ 
                                          / / / _ `/ _  / _ \/ _ \/ / -_)
                                         /_/  \_,_/\_,_/ .__/\___/_/\__/ 
                                                      /_/            
                         ---------------------------------------------------------------
                                                                                       \033[1;m""""""""")

        time.sleep(2)
        print("\033[1;32m [+] wellcome to Tadpole " + user_ID +".\033[1;m ")
        print("\033[1;34m [+]  I'm Hulk here to guide you \033[1;m")
        speak.speak("Wellcome to Tadpole" + user_ID)

def black_eye():
        print("""""""""\033[1;35m

                                       
                                           ___  __         __     ____        
                                          / _ )/ /__ _____/ /__  / __/_ _____ 
                                         / _  / / _ `/ __/  '_/ / _// // / -_)
                                        /____/_/\_,_/\__/_/\_\ /___/\_, /\__/ 
                                                                   /___/      
                            ---------------------------------------------------------------
                                                                                       \033[1;m""""""""")

        time.sleep(2)
        print("\033[1;32m [+] wellcome to Black Eye " + user_ID +".\033[1;m ")
        print("\033[1;34m [+]  I'm Developer here to give you some amzing hints \033[1;m")
        speak.speak("Wellcome to Black eye " + user_ID)

def cigar():
        print("""""""""\033[1;35m

                                       
                                          ______              
                                         / ___(_)__ ____ _____
                                        / /__/ / _ `/ _ `/ __/
                                        \___/_/\_, /\_,_/_/   
                                              /___/           
                            ---------------------------------------------------
                                                                                       \033[1;m""""""""")

        time.sleep(2)
        print("\033[1;32m [+] wellcome to Cigar " + user_ID +".\033[1;m ")
        print("\033[1;34m [+]  I'm Scarlet witch here to guide you \033[1;m")
        speak.speak("Wellcome to Cigar" + user_ID)
 
def Asgard():
        print("""""""""\033[1;35m
                                    _____                                __
                                   /  _  |                              /  /
                                  /  /_| | _____ ____ ______ _______ __/  /
                                 /  ___  |(__ -</ __ '/  __ '/  __/ ___  / 
                                /__/  |__//____/\__, /\__,__/__/  \__,__/
                                               /____/  
                          ----------------------------------------------------------                                            
                                                                      
                                                                       \033[1;m""""""""")
        print("\033[1;32m [+] Wellcome to Asgard \n [+] You are know citizen of the Asgard \033[1;m ")
        speak.speak(" Wellcome to Asgard " + user_ID )
        print("\033[1;32m [+]  Fristly In Asgard you have some conversation with the keeper of the Asgard  and its manditary   \033[1;m")
        speak.speak("Fristly In Asgard you have some conversation with the keeper of the Asgard and  its manditary")
        print("\033[1;32m [+] Asgard Keeper : Hey how are you  \033[1;m")
        speak.speak(" Hey how are you ")
        you = input("\033[1;32m [+] You : \033[1;m")
        if you == user_ID :
                print("\033[1;32m [+] Ooo you come to take stone  \033[1;m ")
        else :
                print("\033[1;31m [+] !!!!--------------------------------Hey you need to maintain your user ID-------------------------!!!!  \033[1;m")
                print("\033[1;31m [+]                                              (Fisrt warnning)                                           \033[1;m")

        
        

        
def Earth():

        print("""""""""\033[1;35m
                                           ______           ___  ___
                                          / ____/___ ______/  /_/  /
                                         / __/ / _  /  ___/ ___/  _ \_
                                        /_____/\_,_/__/   \___/__//_/
                                -----------------------------------------------
                                                                            
                                                                            
                                                                               \033[1;m""""""""")             

        time.sleep(2)
        print("\033[1;32m [+] Wellcome to Earth \033[1;m")
        speak.speak(" Wellcome to Earth ")
        print("\033[1;32m [+] scott : hey buddy its me ant-man \033[1;m")
        time.sleep(1)
        speak.speak("hey buddy its me ant-man")
        print("\033[1;32m [+] scott : whats u r name \033[1;m")
        time.sleep(1)
        speak.speak(" whats your name ")
        n = ""
        while n != user_ID :
                n = input("\033[1;32m [+] A: \033[1;m")
                speak.speak("hey you enter diffrent name than your user_id its k but u need to maintain that id ")
        print("\033[1;32m [+] scott : why did you come here "+ user_ID + " \033[1;m")
        speak.speak(" why did you come here " + user_ID)
        x = input("\033[1;32m [+] A: \033[1;m")
        print("\033[1;32m [+] scott : ok "+ user_ID + " you have one conversation here\033[1;m")
        time.sleep(2)
        earth_chat()
        
                                


def wakanda():
        print("""""""""\033[1;35m
                                         
                                        __      __          __                        .___        
                                       /  \    /  \_____   |  | _______     ____    __| _/_____   
                                       \   \/\/   /\__  \  |  |/ /\__  \   /    \  / __ | \__  \  
                                        \        /  / __ \_|    <  / __ \_|   |  \/ /_/ |  / __ \_
                                         \__/\  /  (____  /|__|_ \(____  /|___|  /\____ | (____  /
                                              \/        \/      \/     \/      \/      \/      \/ 
                ---------------------------------------------------------------------------------------------------------                                                                                               
                                                                                  \033[1;m""""""""""")

        time.sleep(2)
        print("\033[1;32m [+] Wellcome to Wakanda \033[1;m")
        time.sleep(1)
        print("\033[1;34m [+] Wakanda  Forerver\033[1;m")
        time.sleep(1)
        print("\033[1;34m [+] i'm Black panther here to guid you and you have game to play here to \n move next step... here you Go..........\033[1;m")
        time.sleep(3)
        rock_paper()

        speak.speak(" Wellcome to Xandor ")


def tic_toc_to():
        print("***GIVE STAR ONLY IF YOU LIKE***")
        print()
#welcome display
        def Welcome():
            print('   *Welcome to tic-tac-toe game*')
            #dont take sleep more than 2 seconds then user will get bored
            sleep(1)
            print()
            print('Computer will decide who will play first')
            print()
            #for Hint Feature In Computer AI i have passed Player letter instead of computer letter
            print('If you need Hint in the middle of game \npress any of this [Hint,hint,H,h]')
            sleep(1)
            print()
            print('''      *** Format of Game **
                  |    |         1 | 2 | 3
               - - - - - -      - - - - - - 
                  |    |         4 | 5 | 6
               - - - - - -      - - - - - - 
                  |    |         7 | 8 | 9
                                                   ''')


#Fuction to draw Board
#you can modify this sleep method if you dont need it
        def DrawBoard(board,NeedSleep=True):
    #I thought for hint u dont need sleep method so i given default value for Needsleep 
            if NeedSleep:
                sleep(1)
            print()
            print('\033[1;33m             '+board[1]+'  |  '+board[2]+'  |  '+board[3])
            print('             - - - - - - - \033[1;m')
            print('\033[1;33m             '+board[4]+'  |  '+board[5]+'  |  '+board[6])
            print('             - - - - - - - \033[1;m')
            print('\033[1;33m             '+board[7]+'  |  '+board[8]+'  |  '+board[9])
            print('                           \033[1;m')
            print()

#asking the player to choose thier Letter  (X or O)
        def InputPlayerLetter():
            letter=''
    #Ask untill user enters x or o
            while not(letter == 'X' or letter == 'O'):
                print('Do you want to be X or O')
                letter = input().upper()
     
    #returning list bcz of later use
            if letter == 'X':
              return ['X','O']
            if letter == 'O':
              return ['O','X']

#Deciding who should play first randomly
#in usual tic-tac-toe games player first,but it selects randomly between computer and player
        def WhoFirst():
            opponents = ['computer','player']
            if choice(opponents) == 'computer':
                return 'computer'
            else :
                return 'player'
        
#this function asks player to play again
        def PlayAgain():
            print()
            print('Do you want to Play Again (y or n)')
            playagain = input().lower().startswith('y')
            return playagain

#function for making move
        def MakeMove(board,letter,move):
            board[move] = letter

#check if any one win,returns True if wins
#In tic-tac-toe there are 8 possibilities of winning
#horizontal => 3 | vertical => 3 | diagonal => 2
        def IsWinner(board,letter):
            return ( (board[7] == letter and board[8] == letter and board[9] == letter ) or
                     (board[4] == letter and board[5] == letter and board[6] == letter ) or
                     (board[1] == letter and board[2] == letter and board[3] == letter ) or
                     (board[1] == letter and board[4] == letter and board[7] == letter ) or
                     (board[2] == letter and board[5] == letter and board[8] == letter ) or
                     (board[3] == letter and board[6] == letter and board[9] == letter ) or
                     (board[1] == letter and board[5] == letter and board[9] == letter ) or
                     (board[3] == letter and board[5] == letter and board[7] == letter )  )

#duplicate board is useful when we wanted to make temporary changes to the temporary copy of the board without changing the original board
        def GetBoardCopy(board):
            DupeBoard = []
            for i in board:
                DupeBoard.append(i)
            return DupeBoard
    
#fuction to check is space is free
        def IsSpaceFree(board,move):
            return board[move] == ' '

#Getting the player move
        def GetPlayerMove(board):
            move = ''
 
            while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board,int(move)):
                print()
                print('\033[1;32m Enter your move (1 - 9)\033[1;m')
                move = input()
        #if player wants Hint
                if move in HintInput:
                    return move
                    break  
            return int(move)

#choose random move from given list
#it is used when AI  wants to choose out of many possibilities
        def ChooseRandomFromList(board,MoveList):
            PossibleMoves = []
            for i in MoveList:
                if IsSpaceFree(board,i):
                    PossibleMoves.append(i)
            if len(PossibleMoves) != 0:
                return choice(PossibleMoves)
            else:
                return None

#creating computers AI
#this ai works on this algorithm
#1.it checks if computer can win in next move,else
#2.it checks if player can win in next move,then it blocks it,else
#3.it chooses any available spaces from the corner[1,3,7,9],else
#4.it fills middle square if space free,else
#5.it chooses any available spaces from sides,ie,[2,4,6,8]
#if you interchange the 3 and 4 steps the AI becomes little Hard,ie,it fills middle then corner
#--------------------------------------
#Get computer move
        def GetComputerMove(board,ComputerLetter):
            if ComputerLetter == 'X':
                PlayerLetter = 'O'    
            else:
               PlayerLetter = 'X'

    #1.check computer can win in next move
            for i in range(1,10):
                copy = GetBoardCopy(board)
                if IsSpaceFree(copy,i):
                    MakeMove(copy,ComputerLetter,i)
                    if IsWinner(copy,ComputerLetter):
                        return i


    #2.check player can win in next move
            for i in range(1,10):
                copy = GetBoardCopy(board)
                if IsSpaceFree(copy,i):
                    MakeMove(copy,PlayerLetter,i)
                    if IsWinner(copy,PlayerLetter):
                        return i

    #3.checking for corner
            move = ChooseRandomFromList(board,[1,3,7,9])
            if move != None:
                return move
        
    #4.checking for the center
            if IsSpaceFree(board,5):
                return 5
        
    #5.checking for sides
            return ChooseRandomFromList(board,[2,4,6,8])
    
#---------------------------------------   

#checking board is full or not
        def IsBoardFull(board):
            for i in range(1,10):
                if IsSpaceFree(board,i):
                    return False
            return True
            
#fuction to print  the final win or tie board
#made this to separate usual board and winning or tie board
        def FinalBoard(board,NeedSleep=True):
            print('            |-------------|')
            DrawBoard(board,NeedSleep)
            print('            |-------------|')

                    
#LETS START THE GAME
        Welcome()
        while True:
    #intialising board
            TheBoard = [' '] * 10
            PlayerLetter,ComputerLetter = InputPlayerLetter()
            turn = WhoFirst()
            print(f'The {turn} will go first')
    
    #gameloop
            Playing = True
            while Playing:
        
                if turn == 'player':
                    print(f"    Turn => {turn}") 
                    HintInput = ['Hint','hint','H','h'] 
            #taking players input
                    move = GetPlayerMove(TheBoard)
            #if player needs Hint
                    while move in HintInput:                
                #following code gives hint to the user
                #it runs player letter to computer AI
                        HintBox = []
                        for i in TheBoard:
                            HintBox.append(i)
                        hint = GetComputerMove(HintBox,PlayerLetter)
                        MakeMove(HintBox,PlayerLetter,hint)
                        print(f'HINT : placing at {hint} is better')
                        FinalBoard(HintBox,False)
                        move = GetPlayerMove(TheBoard)
              
                    MakeMove(TheBoard,PlayerLetter,move)
            
            
                    if IsWinner(TheBoard,PlayerLetter):
                        FinalBoard(TheBoard)                
                        print('❤You have WON the game❤')
                        scores += 10

                        Playing = not Playing
                    elif IsBoardFull(TheBoard):
                        FinalBoard(TheBoard)
                        print('The game is TIE\nIts good to PLAY untill you WIN❤')
                        print("\033[1;32m [+] if the game was TIE you need to play once either you \n win or lose you need to play or else \n the game will end at this point\033[1;m ")
                        Playing = not Playing
                    else :
                        DrawBoard(TheBoard)
                        turn = 'computer'
 
                else :
            #computer move
                    print(f"    Turn => {turn}")
                    move = GetComputerMove(TheBoard,ComputerLetter)
                    MakeMove(TheBoard,ComputerLetter,move)
            
            
                    if IsWinner(TheBoard,ComputerLetter):
                        FinalBoard(TheBoard)
                        print('❤Try again bro you will win❤')
                        scores -= 2
                        stage_1()
                        Playing = not Playing
                    elif IsBoardFull(TheBoard):
                        FinalBoard(TheBoard)
                        print('The game is TIE\nIts good to PLAY untill you WIN❤')
                        print("\033[1;32m [+] if the game was TIE you need to play once either you \n win or lose you need to play or else \n the game will end at this point\033[1;m ")
                        Playing = not Playing
                    else :
                        DrawBoard(TheBoard)
                        turn = 'player'

            if not PlayAgain():
                print("***❤GIVE STAR ONLY IF YOU LIKE❤***")
                break

def Avenger():              
        print("\033[1;32m [+] Hi " + user_ID + " wellcome  world of stones \033[1;m ")
        speak.speak("  Hi "+ user_ID + "wellcome to world of stones ")

        time.sleep(2)
        print("""\033[1;31m          
                  _
                 / \_   REALITY
                /   \    STONE          
                \___/
                \033[1;m """)
        time.sleep(2)

        print("""\033[1;35m
                  _
                 / \_   POWER       
                /   \   STONE           
                \___/
                \033[1;m """)
        time.sleep(2)
        print("""\033[1;33m
                  _
                 / \_   MIND
                /   \   STONE           
                \___/
                \033[1;m """)
        time.sleep(2)
        print("""\033[1;34m
                  _
                 / \_   SPACE
                /   \   STONE           
                \___/
        \033[1;m """)
        time.sleep(2)
        print("""\033[1;32m
                  _
                 / \_   TIME
                /   \   STONE           
                \___/
        \033[1;m """)
        time.sleep(2)
        print("""\033[1;37m
                  _
                 / \_   SOUL
                /   \   STONE           
                \___/
        \033[1;m """)
        time.sleep(2)

        print("\033[1;32m [+] Avenger are you ready to go....\033[1;m")
        speak.speak("Avenger are  you  ready to go ........")

        time.sleep(3)
        print("""\033[1;33m 

          [0] Asgard 
          [1] Earth 
          [2] tadpole 
          [3] cigar 
          [4] black eye
          [5] andromeda
          [6] Wakanda
          [7] casio
          [8] pin wheel
          [9] whirlpool 
                              \033[1;m """)
        
        time.sleep(1)

        print("\033[1;33m [+] Points : \033[1;m " + str(scores))    
        print("\033[1;33m [+] Stones : \033[1;m " + str(Stons))    
        print("\033[1;32m [+] Where do need to go \033[1;m ")
        speak.speak(" Where do need to go ")
        print(" [+] Enter the numbers of the place like 1 or 2 so on")
        speak.speak("these are the diffrent worlds for hunt  that you  can go any where you want  and the choice is yours   ")
        place = input("\033[1;32m [+] A: \033[1;m")
        if place == "0":
                Asgard()
        elif place == "1":
                Earth()
        elif place == "2":
                tadpole()
        elif place == "3":
                cigar()
        elif place == "4":
                black_eye()
        elif place == "5":
                andromeda()
        elif place == "6":
                wakanda()
        elif place == "7":
                casio()
        elif place == "8":
                pin_wheel()
        elif place == "9":
                whirlpool()

print("""""""""""""""\033[1;31m



                                                   _____                                                  
                                                  /  _  \___  __ ____   ____    ____   ___________  ______
                                                 /  /_\  \  \/ // __ \ /    \  / ___\_/ __ \_  __ \/  ___/
                                                /    |    \   /\  ___/|   |  \/ /_/  >  ___/|  | \/\___ \ 
                                                \____|__  /\_/  \___  >___|  /\___  / \___  >__|  /____  >
                                                        \/          \/     \//_____/      \/           \/ 

                                                L  E  T ' S    B  E  G  I  N    T  H  E     H  U  N  T 
----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                                                                                                     \033[1;m   """"""""""""""")
music()
speak.speak(" use the earphone for the better and best sound effects ")
speak.speak(" welcome to the  avengers ")
time.sleep(3)
print("\033[1;32m [+] Do you want too paly this Game  [ yes/no ] \033[1;m ")
speak.speak(" do you want play this game ")
choice = input("\033[1;32m [+] A: \033[1;m")
if choice ==  "yes" or "y":
        time.sleep(1)
        print("\033[1;32m [+] Hoo that's cool   \033[1;m")
        speak.speak(" Hoo that's cool ")
        print("\033[1;32m\n [+] Enter user ID [it must be any thing that the game  want's  to  knows you]: \033[1;m")
        speak.speak(" enter user ID (it must be any thing that the game  want to  knows you) ")
        user_ID = input("\033[1;32m [+] A:  \033[1;m ")
        scores = 50
        Stons = 0
        Avenger()
elif choice == "no" or "n":
        speak.speak("are you loki side ")
        print(" [-] Are you loki side  ")

 
