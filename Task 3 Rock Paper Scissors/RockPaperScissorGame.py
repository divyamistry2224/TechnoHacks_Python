# Task : Rock, paper, scissors game
# Create a program that allows the user to play
# the classic game of rock, paper, scissors
# against the computer.

# Rock Paper Scissors\assets\blank.png

from tkinter import *
import random

root = Tk()
root.title("ROCK, PAPER, SCISSOR GAME")
root.geometry("640x630+0+0")
root.resizable(0, 0)
root.config(bg="#87C4FF")

# Define images
Blank_img = PhotoImage(file="Task 3 Rock Paper Scissors/assets/blank.png")
Player_Rock = PhotoImage(file="Task 3 Rock Paper Scissors/assets/paper_computer.png")
Player_Rock_ado = Player_Rock.subsample(3, 3)
Player_Paper = PhotoImage(file="Task 3 Rock Paper Scissors/assets/paper_player.png")
Player_Paper_ado = Player_Paper.subsample(3, 3)
Player_Scissor = PhotoImage(file="Task 3 Rock Paper Scissors/assets/rock_computer.png")
Player_Scissor_ado = Player_Scissor.subsample(3, 3)
Computer_Rock = PhotoImage(file="Task 3 Rock Paper Scissors/assets/rock_player.png")
Computer_Paper = PhotoImage(file="Task 3 Rock Paper Scissors/assets/scissor_computer.png")
Computer_Scissor = PhotoImage(file="Task 3 Rock Paper Scissors/assets/scissor_player.png")

# Variables
player_option = 0
games_played = 0
player_wins = 0
computer_wins = 0

# Functions
def update_wins():
    player_label.config(text=f"Player Wins: {player_wins}")
    computer_label.config(text=f"Computer Wins: {computer_wins}")

def Rock():
    global player_option
    player_option = 1
    Image_Player.configure(image=Player_Rock)
    Matching()

def Paper():
    global player_option
    player_option = 2
    Image_Player.configure(image=Player_Paper)
    Matching()

def Scissor():
    global player_option
    player_option = 3
    Image_Player.configure(image=Player_Scissor)
    Matching()

def Comp_Rock():
    global computer_wins, player_wins
    if player_option == 1:
        Label_Status.config(text="Game Tie")
    elif player_option == 2:
        Label_Status.config(text="Player Win")
        player_wins += 1
    elif player_option == 3:
        Label_Status.config(text="Computer Win")
        computer_wins += 1
    update_wins()

def Comp_Paper():
    global computer_wins, player_wins
    if player_option == 1:
        Label_Status.config(text="Computer Win")
        computer_wins += 1
    elif player_option == 2:
        Label_Status.config(text="Game Tie")
    elif player_option == 3:
        Label_Status.config(text="Player Win")
        player_wins += 1
    update_wins()

def Comp_Scissor():
    global computer_wins, player_wins
    if player_option == 1:
        Label_Status.config(text="Player Win")
        player_wins += 1
    elif player_option == 2:
        Label_Status.config(text="Computer Win")
        computer_wins += 1
    elif player_option == 3:
        Label_Status.config(text="Game Tie")
    update_wins()

def Matching():
    computer_option = random.randint(1, 3)
    if computer_option == 1:
        Image_Computer.configure(image=Computer_Rock)
        Comp_Rock()
    elif computer_option == 2:
        Image_Computer.configure(image=Computer_Paper)
        Comp_Paper()
    elif computer_option == 3:
        Image_Computer.configure(image=Computer_Scissor)
        Comp_Scissor()

def Exit():
    root.destroy()
    exit()

Image_Player = Label(root, image=Blank_img)
Image_Computer = Label(root, image=Blank_img)
Label_Player = Label(root, text="PLAYER", font=('Arial', 19, 'bold'), bg="#192655", fg="white")
Label_Player.grid(row=1, column=1)
Label_Computer = Label(root, text="COMPUTER", font=('Arial', 19, 'bold'), bg="#192655", fg="white")
Label_Computer.grid(row=1, column=3)
Label_Status = Label(root, text="", font=('Times New Roman', 18))
Label_Status.grid(row=3, column=2)
Image_Player.grid(row=2, column=1, padx=30, pady=20)
Image_Computer.grid(row=2, column=3, pady=20)
player_label = Label(root, text=f"Player Wins: {player_wins}")
player_label.grid(row=6, column=1)
computer_label = Label(root, text=f"Computer Wins: {computer_wins}")
computer_label.grid(row=6, column=3)

rock = Button(root, image=Player_Rock_ado, command=Rock)
paper = Button(root, image=Player_Paper_ado, command=Paper)
scissor = Button(root, image=Player_Scissor_ado, command=Scissor)
button_quit = Button(root, text="Quit", bg="red", fg="white", font=('Times New Roman', 25, 'bold'), command=Exit)
rock.grid(row=4, column=1, pady=30)
paper.grid(row=4, column=2, pady=30)
scissor.grid(row=4, column=3, pady=30)
button_quit.grid(row=7, column=2)

root.mainloop()