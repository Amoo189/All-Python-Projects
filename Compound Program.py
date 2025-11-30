# pip install PyAutoGUI
# pip install plyer
#POWERED BY SALEH AMOO||I CREAT THIS PROGRAM ASAP
print('SALEH AMOO:THIS PROGRAM JUST SUPORT ON WINDOWS,MAC OS,LINUX||THIS PROGRAM NOT SUPORT ON ANDROID||install <plyer> library and after that install <pyautogui> library{on your PC}')
from plyer import notification
notification_title = "SALEH AMOO:"
notification_message = "wellcome to our program||this program written by SALEH AMOO||FROM THE ISLAMIC REPUBLIC OF IRAN"
notification_duration = 30
notification.notify(
title=notification_title,
message=notification_message,
timeout=notification_duration
)
import pyautogui,sys
from math import*
import sys
pyautogui.alert('This is a message from saleh amoo for you.', 'SALEH AMOO')
gg=pyautogui.prompt('Do you want to continue?no/everything', "SALEH AMOO")
if gg=='no':
   from plyer import notification
   notification_title = "SALEH AMOO:"
   notification_message = "BYE"
   notification_duration = 3  
   notification.notify(
   title=notification_title,
   message=notification_message,
   timeout=notification_duration
   )
   sys.exit()
m = pyautogui.prompt("What is your name?", "AI")
pyautogui.alert('wellcome %s'%(m), 'SALEH AMOO')
p=pyautogui.password('What is the password?', 'CHAT DSA')
pyautogui.alert('you with %s name and %s password exces' %(m,p), 'SALEH AMOO')
H = pyautogui.prompt("what do you want(SKVD,MATH,STR,BICAIPY,CHAT DSA,RPG,RDA,CLOCK,TTT,TTTpro,COF,CNMF,PNAA,GDNG,DINO,soon...)", "AI")
if H=="SKVD":
   db = {}
   pyautogui.confirm('Welcome to the simplest key-value database')
   while True:
      pyautogui.confirm('What do you want to do?')
      action=pyautogui.prompt('Enter P to [P]ut, G to [G]et or L to [L]ist Or enter Q to [Q]uit')
      if action == 'P':
          k = pyautogui.prompt('Enter key: ')
          d = pyautogui.prompt('Enter data: ')
          db[k] = d
      elif action == 'G':
          k = pyautogui.prompt('Enter key: ')
          if not k in db:
                  pyautogui.confirm('No such key')
          else:
              pyautogui.confirm('Your data: %s' % db[k])
      elif action == 'L':
        pyautogui.confirm('DB contents:')
        pyautogui.confirm(db)
      elif action == 'Q':
        
        from plyer import notification
        notification_title = "SALEH AMOO:"
        notification_message = "BYE"
        notification_duration = 3  
        notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_duration
        )
        break
if H=='PNAA':
    a = 0
    b = 0
    pyautogui.confirm("Welcome to the p number accuracy app!")
    pyautogui.confirm("Increase the accuracy of the number from 10000 to... (the desired number)")
    n = int(pyautogui.prompt("Enter p number accuracy:"))
    pyautogui.confirm("wait...")
    for i in range(1, n, 4):
	    a = a + 1 / i
    for j in range(3, n, 4):
	    b = b + 1 / j
    pyautogui.confirm(4*(a-b))
if H=='RPG':
    from random import randint 
    pyautogui.confirm("Welcome to the random password generator program")
    char = ["3", "5", "s", "6", "M", "S", "1", "a", "b", "c", '$' ,'#', '^', '%']
    password = ""
    n = int(pyautogui.prompt('Enter range of password:'))
    for i in range (n):
        key = randint(1, len(char))
        password = password + char[key-1]
    pyautogui.confirm(password);
    pyautogui.confirm("Password maked.");
    sys.exit()
    from plyer import notification
    notification_title = "SALEH AMOO:"
    notification_message = "BYE||PROGRAM CLOCED||POWERDE BY SALEH AMOO."
    notification_duration = 3  
    notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_duration
    )

if H=='MATH':
    from math import *
    pyautogui.confirm('This program can calculate pi number, e number, fabs of  number,floor of  number,ceil of  number,factorial,cos,sin,log of two numbers, pow of two number,sqrt of number,hypot of two numbers,radians,degrees,tan,gcd,lcm.Q FOR END')

    while True:
        pyautogui.confirm('Help:pi for pi,e for e,f for fabs,fl for floor,c for ceil,! for factorial, cos for cos,sin for sin,l  for log,po for pow, sq for sqrt,hy for hypot,radi for radians, degr for degrees||lcm,gcd.')
        o = pyautogui.prompt("Now,What do you want?:")
        if o == 'pi':
            pyautogui.confirm(f"The answer:{pi}")
        if o == 'e':
            pyautogui.confirm(f"The answer:{e}")
        if o == 'f':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{fabs(    fa)}")
        if o == 'fl':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{floor(    fa)}")
        if o == 'c':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{ceil(    fa)}")
        if o == '!':
            fa = int(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{factorial(    fa)}")
        if o == 'cos':
            fa = int(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{cos(    fa)}")
        if o == 'sin':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{sin(    fa)}")
        if o == 'l':
            fa = float(pyautogui.prompt("Enter your number:"))
       # fas = float(pyautogui.prompt("Enter your second number:"))
            pyautogui.confirm(f"The answer is:{log(    fa)}")
        if o == 'po':
            fa = float(pyautogui.prompt("Enter your first number:"))
            fas = float(pyautogui.prompt("Enter your second number:"))
            pyautogui.confirm(f"The answer is:{pow(fa,fas)}")
        if o == 'sq':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{sqrt(fa)}")
        if o == 'hy':
            fa = float(pyautogui.prompt("Enter your first number:"))
            fas = float(pyautogui.prompt("Enter your second number:"))
            pyautogui.confirm(f"The answer is:{hypot(    fa, fas)}")
        if o == 'radi':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{radians(    fa)}")
        if o == 'degr':
            fa = float(pyautogui.prompt("Enter your number:"))
            pyautogui.confirm(f"The answer is:{degrees(    fa)}")
        if o == 'tan':
            fa = int(pyautogui.prompt('Enter your number:'))
            pyautogui.confirm(f"The answer is:{tan(    fa)}")
        if o=="gcd":
            fa = float(pyautogui.prompt("Enter your number:"))
            fas = float(pyautogui.prompt("Enter your second number:"))
            pyautogui.confirm(f"The answer is:{gcd(    fa,fac)}")
        if o=="lcm":
            fa = float(pyautogui.prompt("Enter your number:"))
            fas = float(pyautogui.prompt("Enter your second number:"))
            pyautogui.confirm(f"The answer is:{lcm(    fa,fac)}")
        if o=="Q":
           sys.exit()
           from plyer import notification
           notification_title = "SALEH AMOO:"
           notification_message = "BYE||PROGRAM CLOCED."
           notification_duration = 3  
           notification.notify(
           title=notification_title,
           message=notification_message,
           timeout=notification_duration
           )

if H=='COF':
    pyautogui.confirm("Welcome to calculate of factoriel app")
    n = int(pyautogui.prompt("Enter the number:"))
    d = 1
    a = 1
    while a < n+1:
        d = d * a
        a = a + 1
#pyautogui.confirm(d)
    pyautogui.confirm(f"{d:,}")
    from plyer import notification
    notification_title = "SALEH AMOO:"
    notification_message = "BYE||PROGRAM CLOCED||POWERDE BY SALEH AMOO."
    notification_duration = 3  
    notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_duration
    )

if H=='STR':
    import pyttsx3
    import sys
    voice = pyttsx3.init()
    voice.setProperty('rate', 130)
    voice.setProperty('volume', 0.75)
    #voice.setProperty('voice')
    voice.say("wellcome to speech text with R2 program")
    voice.say("Iam R2")
#voice.say("you can asking anything ")
    while True:
        text = pyautogui.prompt('Enter the word you want to speake:')           
        voice.setProperty('rate', 130)
        voice.say(f"your word:{text}")
        voice.setProperty('volume', 0.5) 
        voice.runAndWait()
    if text=="Q":
        sys.exit() 
if H=='BICAIPY':
    pyautogui.confirm("Welcome to the bank interest calculation program according to interest percentage and year||Q for end")
    balance = int(pyautogui.prompt('Enter your balance||Q:')) 
    bank_interest = int(pyautogui.prompt('Enter your bank interest||Q:')) 
    year = int(pyautogui.prompt('How many years?||Q:')) 
    if balance or year or bank_interest=='Q':
        sys.exit()
    for i in range(year):
        balance = balance + bank_interest/100 * balance
    pyautogui.confirm(balance)
    pyautogui.confirm ("Thank you for choose we're app!")
    from plyer import notification
    notification_title = "SALEH AMOO:"
    notification_message = "BYE||PROGRAM CLOCED||POWERDE BY SALEH AMOO."
    notification_duration = 3  
    notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_duration
    )
if H=='CHAT DSA':
    import pyttsx3
    import wikipedia
    voice = pyttsx3.init()
    pyautogui.alert('THIS PART OF PROGRAM NEED INTERNET','CHAT DSA')
    voice.setProperty('rate', 130)
    voice.setProperty('volume', 0.5)
    voice.say("Wellcome to artificial intelligence asking R2 app")
    voice.say("iam r2")
    voice.say("TURN ON YOUR INTERNET")
#voice.say("you can asking anything ")
    while True:
        text = pyautogui.prompt('Enter the word you want to search for/<TURN ON YOUR INTERNET>/:')
        result = wikipedia.summary(text, sentences=3)
        pyautogui.confirm(result)    
        voice.setProperty('rate', 130)
        voice.setProperty('volume', 0.5) 
        voice.say(result)
        voice.runAndWait()
if H=='TTT':
    from tkinter import *
    import tkinter.messagebox
    tk = Tk()
    tk.title("Tic Tac Toe")
    click = True
    def checker(buttons):
        global click
        if buttons["text"] == " " and click == True:
            buttons["text"] = "X"
            click = False
        elif buttons["text"] == " " and click == False:
            buttons["text"] = "O"
            click = True
        elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
              button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
              button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
              button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
              button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
              button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
              button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
              button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
              tkinter.messagebox.showinfo("SALEH AMOO", "X Won the game")
        elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
                button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
                button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
                button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
                button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
                button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
                button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
                button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
                tkinter.messagebox.showinfo("SALEH AMOO", "O Won the game")
    buttons=StringVar()
    button1 = Button(tk,text= " " ,font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button1))
    button1.grid(row=1, column=0, sticky = S+N+E+W)
    button2 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button2))
    button2.grid(row = 1, column =1, sticky = S+N+E+W)
    button3 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button3))
    button3.grid(row = 1, column =2, sticky = S+N+E+W)
    button4 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command =lambda:checker(button4)) 
    button4.grid(row = 2, column =0, sticky = S+N+E+W)
    button5 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button5))
    button5.grid(row = 2, column =1, sticky = S+N+E+W)
    button6 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button6))
    button6.grid(row = 2, column =2, sticky = S+N+E+W)
    button7 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button7))
    button7.grid(row = 3, column =0, sticky = S+N+E+W)
    button8 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button8))
    button8.grid(row = 3, column =1, sticky = S+N+E+W)    
    button9 = Button(tk,text= " " , font=('Times 26 bold'), height = 4, width = 8 , command=lambda:checker(button9))
    button9.grid(row = 3, column =2, sticky = S+N+E+W)
    tk.mainloop()
    from plyer import notification
    notification_title = "SALEH AMOO:"
    notification_message = "BYE||PROGRAM CLOCED||POWERDE BY SALEH AMOO."
    notification_duration = 3  
    notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_duration
    )
if H=='CLOCK':
    from tkinter import Label, Tk 
    import time
    app_window = Tk() 
    app_window.title("Digital Clock||saleh amoo") 
    app_window.geometry("400x133") 
    app_window.resizable(0,0)
    text_font= ("Times New Roman (Headings CS)", 58, 'bold')
    background = "#87CEFA"
    foreground= "#191970"
    border_width = 54
    label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
    label.grid(row=0, column=1)
    def digital_clock(): 
       time_live = time.strftime("%H:%M:%S")
       label.config(text=time_live) 
       label.after(200, digital_clock)

    digital_clock()
    app_window.mainloop()

if H=='RDA':
    pyautogui.confirm("Welcome to rolling dices app.")
    import random 
    a = 1 
    b = 6
    rolling_again = "yes"
    while rolling_again == 'yes' or rolling_again == "yes":
        pyautogui.confirm('Dices rolling...')
        pyautogui.confirm(f"The value are:{random. randint(a , b)}")
        rolling_again = input("rolling the dices again?:")
    if rolling_again == 'no':
        pyautogui.confirm("The end")
        from plyer import notification
        notification_title = "SALEH AMOO:"
        notification_message = "BYE||PROGRAM CLOCED||POWERDE BY SALEH AMOO."
        notification_duration = 5  
        notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_duration
        )

if H=='CNMF':
    pyautogui.confirm("Welcome to calculate n mold fibonachi app. ")
    n = int(input('Enter the n: '))
    a = 1
    b = 1
    c = 0
    i = 2
    while i < n:
        c = a + b
        a = b
        b = c
        i = i + 1
    pyautogui.confirm(c)
    from plyer import notification
    notification_title = "SALEH AMOO:"
    notification_message = "BYE||PROGRAM CLOCED||POWERDE BY SALEH AMOO."
    notification_duration = 3  
    notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_duration
    )

if H=='TTTpro':
    from tkinter import *
    import numpy as np
    size_of_board = 600
    symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
    symbol_thickness = 50
    symbol_X_color = '#EE4035'
    symbol_O_color = '#0492CF'
    Green_color = '#7BC043'
    class Tic_Tac_Toe():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
        def __init__(self):
            self.window = Tk()
            self.window.title('Tic-Tac-Toe||SALEH AMOO')
            self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
            self.canvas.pack()
        # Input from user in form of clicks
            self.window.bind('<Button-1>', self.click)

            self.initialize_board()
            self.player_X_turns = True
            self.board_status = np.zeros(shape=(3, 3))

            self.player_X_starts = True
            self.reset_board = False
            self.gameover = False
            self.tie = False
            self.X_wins = False
            self.O_wins = False

            self.X_score = 0
            self.O_score = 0
            self.tie_score = 0

        def mainloop(self):
            self.window.mainloop()

        def initialize_board(self):
            for i in range(2):
                self.canvas.create_line((i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

            for i in range(2):
                self.canvas.create_line(0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

        def play_again(self):
           self.initialize_board()
           self.player_X_starts = not self.player_X_starts
           self.player_X_turns = self.player_X_starts
           self.board_status = np.zeros(shape=(3, 3))
           

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------

        def draw_O(self, logical_position):
            logical_position = np.array(logical_position)
        # logical_position = grid value on the board
        # grid_position = actual pixel values of the center of the grid
            grid_position = self.convert_logical_to_grid_position(logical_position)
            self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    outline=symbol_O_color)

        def draw_X(self, logical_position):
            grid_position = self.convert_logical_to_grid_position(logical_position)
            self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    fill=symbol_X_color)
            self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                    fill=symbol_X_color)

        def display_gameover(self):

            if self.X_wins:
                self.X_score += 1
                text = 'X WIN'
                color = symbol_X_color
            elif self.O_wins:
                self.O_score += 1
                text = 'O WIN'
                color = symbol_O_color
            else:
                self.tie_score += 1
                text = 'Its a tie'
                color = 'gray'

            self.canvas.delete("all")
            self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

            score_text = 'Scores \n'
            self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                    text=score_text)

            score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
            score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
            score_text += 'Tie                    : ' + str(self.tie_score)
            self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                    text=score_text)
            self.reset_board = True

            score_text = 'Click to play again \n'
            self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                    text=score_text)

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

        def convert_logical_to_grid_position(self, logical_position):
            logical_position = np.array(logical_position, dtype=int)
            return (size_of_board / 3) * logical_position + size_of_board / 6

        def convert_grid_to_logical_position(self, grid_position):
            grid_position = np.array(grid_position)
            return np.array(grid_position // (size_of_board / 3), dtype=int)

        def is_grid_occupied(self, logical_position):
            if self.board_status[logical_position[0]][logical_position[1]] == 0:
                return False
            else:
                return True

        def is_winner(self, player):
            player = -1 if player == 'X' else 1

        # Three in a row
            for i in range(3):
                if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                    return True
                if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                    return True

        # Diagonals
            if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                return True

            if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                return True

            return False

        def is_tie(self):

            r, c = np.where(self.board_status == 0)
            tie = False
            if len(r) == 0:
                tie = True

            return tie

        def is_gameover(self):
        # Either someone wins or all grid occupied
            self.X_wins = self.is_winner('X')
            if not self.X_wins:
                self.O_wins = self.is_winner('O')

            if not self.O_wins:
                self.tie = self.is_tie()

            gameover = self.X_wins or self.O_wins or self.tie

            if self.X_wins:
                pyautogui.confirm('X wins')
            if self.O_wins:
                pyautogui.confirm('O wins')
            if self.tie:
                pyautogui.confirm('Its a tie')

            return gameover





        def click(self, event):
            grid_position = [event.x, event.y]
            logical_position = self.convert_grid_to_logical_position(grid_position)

            if not self.reset_board:
                if self.player_X_turns:
                   if not self.is_grid_occupied(logical_position):
                        self.draw_X(logical_position)
                        self.board_status[logical_position[0]][logical_position[1]] = -1
                        self.player_X_turns = not self.player_X_turns
                else:
                    if not self.is_grid_occupied(logical_position):
                        self.draw_O(logical_position)
                        self.board_status[logical_position[0]][logical_position[1]] = 1
                        self.player_X_turns = not self.player_X_turns

            # Check if game is concluded
                if self.is_gameover():
                    self.display_gameover()
                # pyautogui.confirm('Done')
            else:  # Play Again
                self.canvas.delete("all")
                self.play_again()
                self.reset_board = False


    game_instance = Tic_Tac_Toe()
    game_instance.mainloop()
if H=='DINO':
    pyautogui.alert('this program just open on WIN and MAC OS not android!~~~.install plyer library and pygame.')
    from plyer import notification
    notification_title = "SALEH AMOO:"
    notification_message = "First, get the _(sprites)_ file from Saleh Amoo."
    notification_duration = 180  
    notification.notify(
    title=notification_title,
    message=notification_message,
    timeout=notification_duration
    )
    __author__ = "Saleh Amoo"
    import os
    import sys
    import pygame
    import random
    from pygame import *
    pygame.init()
    scr_size = (width,height) = (600,150)
    FPS = 60
    gravity = 0.6
    black = (0,0,0)
    white = (255,255,255)
    background_col = (235,235,235)
    high_score = 9999
    screen = pygame.display.set_mode(scr_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("DINO||SALEH AMOO")
    jump_sound = pygame.mixer.Sound('jump.wav')
    die_sound = pygame.mixer.Sound('die.wav')
    checkPoint_sound = pygame.mixer.Sound('checkPoint.wav')
    def load_image(
        name,
        sizex=-1,
        sizey=-1,
        colorkey=None,
        ):

        fullname = os.path.join('sprites', name)
        image = pygame.image.load(fullname)
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)

        if sizex != -1 or sizey != -1:
            image = pygame.transform.scale(image, (sizex, sizey))

        return (image, image.get_rect())

    def load_sprite_sheet(
            sheetname,
            nx,
            ny,
            scalex = -1,
            scaley = -1,
            colorkey = None,
            ):
        fullname = os.path.join('sprites',sheetname)
        sheet = pygame.image.load(fullname)
        sheet = sheet.convert()

        sheet_rect = sheet.get_rect()

        sprites = []

        sizex = sheet_rect.width/nx
        sizey = sheet_rect.height/ny

        for i in range(0,ny):
            for j in range(0,nx):
                rect = pygame.Rect((j*sizex,i*sizey,sizex,sizey))
                image = pygame.Surface(rect.size)
                image = image.convert()
                image.blit(sheet,(0,0),rect)

                if colorkey is not None:
                    if colorkey is -1:
                        colorkey = image.get_at((0,0))
                    image.set_colorkey(colorkey,RLEACCEL)

                if scalex != -1 or scaley != -1:
                    image = pygame.transform.scale(image,(scalex,scaley))

                sprites.append(image)

        sprite_rect = sprites[0].get_rect()

        return sprites,sprite_rect

    def disp_gameOver_msg(retbutton_image,gameover_image):
        retbutton_rect = retbutton_image.get_rect()
        retbutton_rect.centerx = width / 2
        retbutton_rect.top = height*0.52

        gameover_rect = gameover_image.get_rect()
        gameover_rect.centerx = width / 2
        gameover_rect.centery = height*0.35

        screen.blit(retbutton_image, retbutton_rect)
        screen.blit(gameover_image, gameover_rect)

    def extractDigits(number):
        if number > -1:
            digits = []
            i = 0
            while(number/10 != 0):
                digits.append(number%10)
                number = int(number/10)

            digits.append(number%10)
            for i in range(len(digits),5):
                digits.append(0)
            digits.reverse()
            return digits

    class Dino():
        def __init__(self,sizex=-1,sizey=-1):
            self.images,self.rect = load_sprite_sheet('dino.png',5,1,sizex,sizey,-1)
            self.images1,self.rect1 = load_sprite_sheet('1.png',2,1,60,sizey,-1)
            self.rect.bottom = int(0.98*height)
            self.rect.left = width/15
            self.image = self.images[0]
            self.index = 0
            self.counter = 0
            self.score = 0
            self.isJumping = False
            self.isDead = False
            self.isDucking = False
            self.isBlinking = False
            self.movement = [0,0]
            self.jumpSpeed = 11.5

            self.stand_pos_width = self.rect.width
            self.duck_pos_width = self.rect1.width

        def draw(self):
            screen.blit(self.image,self.rect)

        def checkbounds(self):
            if self.rect.bottom > int(0.98*height):
                self.rect.bottom = int(0.98*height)
                self.isJumping = False

        def update(self):
            if self.isJumping:
                self.movement[1] = self.movement[1] + gravity

            if self.isJumping:
                self.index = 0
            elif self.isBlinking:
                if self.index == 0:
                    if self.counter % 400 == 399:
                        self.index = (self.index + 1)%2
                else:
                    if self.counter % 20 == 19:
                        self.index = (self.index + 1)%2

            elif self.isDucking:
                if self.counter % 5 == 0:
                    self.index = (self.index + 1)%2
            else:
                if self.counter % 5 == 0:
                    self.index = (self.index + 1)%2 + 2

            if self.isDead:
               self.index = 4

            if not self.isDucking:
                self.image = self.images[self.index]
                self.rect.width = self.stand_pos_width
            else:
                self.image = self.images1[(self.index)%2]
                self.rect.width = self.duck_pos_width

            self.rect = self.rect.move(self.movement)
            self.checkbounds()

            if not self.isDead and self.counter % 7 == 6 and self.isBlinking == False:
                self.score += 1
                if self.score % 100 == 0 and self.score != 0:
                    if pygame.mixer.get_init() != None:
                        checkPoint_sound.play()

            self.counter = (self.counter + 1)

    class Cactus(pygame.sprite.Sprite):
        def __init__(self,speed=5,sizex=-1,sizey=-1):
            pygame.sprite.Sprite.__init__(self,self.containers)
            self.images,self.rect = load_sprite_sheet('cacti-small.png',3,1,sizex,sizey,-1)
            self.rect.bottom = int(0.98*height)
            self.rect.left = width + self.rect.width
            self.image = self.images[random.randrange(0,3)]
            self.movement = [-1*speed,0]

        def draw(self):
            screen.blit(self.image,self.rect)

        def update(self):
            self.rect = self.rect.move(self.movement)

            if self.rect.right < 0:
                self.kill()

    class Ptera(pygame.sprite.Sprite):
        def __init__(self,speed=5,sizex=-1,sizey=-1):
            pygame.sprite.Sprite.__init__(self,self.containers)
            self.images,self.rect = load_sprite_sheet('ptera.png',2,1,sizex,sizey,-1)
            self.ptera_height = [height*0.82,height*0.75,height*0.60]
            self.rect.centery = self.ptera_height[random.randrange(0,3)]
            self.rect.left = width + self.rect.width
            self.image = self.images[0]
            self.movement = [-1*speed,0]
            self.index = 0
            self.counter = 0

        def draw(self):
            screen.blit(self.image,self.rect)

        def update(self):
            if self.counter % 10 == 0:
                self.index = (self.index+1)%2
            self.image = self.images[self.index]
            self.rect = self.rect.move(self.movement)
            self.counter = (self.counter + 1)
            if self.rect.right < 0:
                self.kill()


    class Ground():
        def __init__(self,speed=-5):
            self.image,self.rect = load_image('ground.png',-1,-1,-1)
            self.image1,self.rect1 = load_image('ground.png',-1,-1,-1)
            self.rect.bottom = height
            self.rect1.bottom = height
            self.rect1.left = self.rect.right
            self.speed = speed

        def draw(self):
            screen.blit(self.image,self.rect)
            screen.blit(self.image1,self.rect1)

        def update(self):
            self.rect.left += self.speed
            self.rect1.left += self.speed

            if self.rect.right < 0:
                self.rect.left = self.rect1.right

            if self.rect1.right < 0:
                self.rect1.left = self.rect.right

    class Cloud(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self,self.containers)
            self.image,self.rect = load_image('cloud.png',int(90*30/42),30,-1)
            self.speed = 1
            self.rect.left = x
            self.rect.top = y
            self.movement = [-1*self.speed,0]

        def draw(self):
            screen.blit(self.image,self.rect)

        def update(self):
            self.rect = self.rect.move(self.movement)
            if self.rect.right < 0:
                self.kill()

    class Scoreboard():
        def __init__(self,x=-1,y=-1):
            self.score = 0
            self.tempimages,self.temprect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
            self.image = pygame.Surface((55,int(11*6/5)))
            self.rect = self.image.get_rect()
            if x == -1:
                self.rect.left = width*0.89
            else:
                self.rect.left = x
            if y == -1:
                self.rect.top = height*0.1
            else:
                self.rect.top = y

        def draw(self):
            screen.blit(self.image,self.rect)

        def update(self,score):
            score_digits = extractDigits(score)
            self.image.fill(background_col)
            for s in score_digits:
                self.image.blit(self.tempimages[s],self.temprect)
                self.temprect.left += self.temprect.width
            self.temprect.left = 0


    def introscreen():
        temp_dino = Dino(44,47)
        temp_dino.isBlinking = True
        gameStart = False

        temp_ground,temp_ground_rect = load_sprite_sheet('ground.png',15,1,-1,-1,-1)
        temp_ground_rect.left = width/20
        temp_ground_rect.bottom = height

        logo,logo_rect = load_image('logo3.png',300,140,-1)
        logo_rect.centerx = width*0.6
        logo_rect.centery = height*0.6
        while not gameStart:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                return True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                            temp_dino.isJumping = True
                            temp_dino.isBlinking = False
                            temp_dino.movement[1] = -1*temp_dino.jumpSpeed

            temp_dino.update()
 
            if pygame.display.get_surface() != None:
                screen.fill(background_col)
                screen.blit(temp_ground[0],temp_ground_rect)
                if temp_dino.isBlinking:
                    screen.blit(logo,logo_rect)
                temp_dino.draw()

                pygame.display.update()

            clock.tick(FPS)
            if temp_dino.isJumping == False and temp_dino.isBlinking == False:
                gameStart = True

    def gameplay():
        global high_score
        gamespeed = 4
        startMenu = False
        gameOver = False
        gameQuit = False
        playerDino = Dino(44,47)
        new_ground = Ground(-1*gamespeed)
        scb = Scoreboard()
        highsc = Scoreboard(width*0.78)
        counter = 0

        cacti = pygame.sprite.Group()
        pteras = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        last_obstacle = pygame.sprite.Group()

        Cactus.containers = cacti
        Ptera.containers = pteras
        Cloud.containers = clouds
 
        retbutton_image,retbutton_rect = load_image('replay_button.png',35,31,-1)
        gameover_image,gameover_rect = load_image('game_over.png',190,11,-1)

        temp_images,temp_rect = load_sprite_sheet('numbers.png',12,1,11,int(11*6/5),-1)
        HI_image = pygame.Surface((22,int(11*6/5)))
        HI_rect = HI_image.get_rect()
        HI_image.fill(background_col)
        HI_image.blit(temp_images[10],temp_rect)
        temp_rect.left += temp_rect.width
        HI_image.blit(temp_images[11],temp_rect)
        HI_rect.top = height*0.1
        HI_rect.left = width*0.73

        while not gameQuit:
            while startMenu:
                pass
            while not gameOver:
                if pygame.display.get_surface() == None:
                    print("Couldn't load display surface")
                    gameQuit = True
                    gameOver = True
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameQuit = True
                            gameOver = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                if playerDino.rect.bottom == int(0.98*height):
                                    playerDino.isJumping = True
                                    if pygame.mixer.get_init() != None:
                                        jump_sound.play()
                                    playerDino.movement[1] = -1*playerDino.jumpSpeed

                            if event.key == pygame.K_DOWN:
                                if not (playerDino.isJumping and playerDino.isDead):
                                    playerDino.isDucking = True

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_DOWN:
                                playerDino.isDucking = False
                for c in cacti:
                    c.movement[0] = -1*gamespeed
                    if pygame.sprite.collide_mask(playerDino,c):
                        playerDino.isDead = True
                        if pygame.mixer.get_init() != None:
                            die_sound.play()

                for p in pteras:
                    p.movement[0] = -1*gamespeed
                    if pygame.sprite.collide_mask(playerDino,p):
                        playerDino.isDead = True
                        if pygame.mixer.get_init() != None:
                            die_sound.play()

                if len(cacti) < 2:
                    if len(cacti) == 0:
                        last_obstacle.empty()
                        last_obstacle.add(Cactus(gamespeed,40,40))
                    else:
                        for l in last_obstacle:
                            if l.rect.right < width*0.7 and random.randrange(0,50) == 10:
                                last_obstacle.empty()
                                last_obstacle.add(Cactus(gamespeed, 40, 40))

                if len(pteras) == 0 and random.randrange(0,200) == 10 and counter > 500:
                    for l in last_obstacle:
                        if l.rect.right < width*0.8:
                            last_obstacle.empty()
                            last_obstacle.add(Ptera(gamespeed, 46, 40))

                if len(clouds) < 5 and random.randrange(0,300) == 10:
                    Cloud(width,random.randrange(height/5,height/2))

                playerDino.update()
                cacti.update()
                pteras.update()
                clouds.update()
                new_ground.update()
                scb.update(playerDino.score)
                highsc.update(high_score)

                if pygame.display.get_surface() != None:
                    screen.fill(background_col)
                    new_ground.draw()
                    clouds.draw(screen)
                    scb.draw()
                    if high_score != 0:
                        highsc.draw()
                        screen.blit(HI_image,HI_rect)
                    cacti.draw(screen)
                    pteras.draw(screen)
                    playerDino.draw()

                    pygame.display.update()
                clock.tick(FPS)

                if playerDino.isDead:
                    gameOver = True
                    if playerDino.score > high_score:
                        high_score = playerDino.score

                if counter%700 == 699:
                    new_ground.speed -= 1
                    gamespeed += 1

                counter = (counter + 1)

            if gameQuit:
                break

            while gameOver:
                if pygame.display.get_surface() == None:
                    print("Couldn't load display surface")
                    gameQuit = True
                    gameOver = False
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameQuit = True
                            gameOver = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                gameQuit = True
                                gameOver = False

                            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                                gameOver = False
                                gameplay()
                highsc.update(high_score)
                if pygame.display.get_surface() != None:
                    disp_gameOver_msg(retbutton_image,gameover_image)
                    if high_score != 0:
                        highsc.draw()
                        screen.blit(HI_image,HI_rect)
                    pygame.display.update()
                clock.tick(FPS)

        pygame.quit()
        quit()

    def main():
        isGameQuit = introscreen()
        if not isGameQuit:
            gameplay()

    main()
