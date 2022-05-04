#!/sbin/python3

import tkinter as tk
import random
# import playsound TODO: Add sound
from scoring_functions import *

window = tk.Tk()
window.title("Yahtzee! World")
window.geometry("700x300")

yahtzee_count = 0

# Create the list of images and the canvas
dice_images = []
for i in range(1,7):
  dice_images.append(tk.PhotoImage(file = str(i) + ".gif"))

# Create the dice_rolls list
dice_rolls = []
# Create the canvas list
canvas_list = []
for i in range(5):
    roll = random.randint(1,6)
    dice_rolls.append(roll)
    canvas_list.append(tk.Canvas(
        window,
        width=100,
        height=100,
    ))
    canvas_list[i].grid(row=0,column = i)
    canvas_list[i].create_image(
        0,
        0,
        anchor=tk.NW,
        image = dice_images[dice_rolls[i] - 1]
    )

def roll_dice():
    for i in range(5):
        if enable[i].get() == 0:
            roll = random.randint(0,5)
            # update the dice_rolls
            dice_rolls[i] = roll + 1
            canvas_list[i].create_image(
                0,
                0,
                anchor=tk.NW,
            image = dice_images[roll]
        )
    score_helper()

# Score helper function
def score_helper():
    global yahtzee_count
    # Labels for the scores (small straights, large straights, full house, etc.)
    lbl_chance['text'] = "Chance: "+str(chance(dice_rolls))
    lbl_threes['text'] = "Three of a kind: "+str(three_of_kind(dice_rolls))
    lbl_fours['text'] = "Four of a kind: "+str(four_of_kind(dice_rolls))
    lbl_fulls['text'] = "Full house: "+str(full_house(dice_rolls))
    lbl_sm['text'] = "Small straight: "+str(sm_straight(dice_rolls))
    lbl_lg['text'] = "Large straight: "+str(lg_straight(dice_rolls))
    lbl_yahtzee['text'] = "Yahtzee!: "+str(yahtzee(dice_rolls) + (100 * yahtzee_count))
    # Update the singles lables
    for i,lbl in enumerate(lbl_singles):
      lbl['text'] = str(i+1) + "'s: " + str(singles(dice_rolls,i+1))

    # Count the number of Yahtzee's to add the additional 100 pts per yahtzee
    if yahtzee(dice_rolls) > 0:
        yahtzee_count += 1

chkBox_list = []

enable = {
     0:tk.IntVar(),
     1:tk.IntVar(),
     2:tk.IntVar(),
     3:tk.IntVar(),
     4:tk.IntVar(),
}

for i in range(5):
    # create and append new checkbox
    chkBox_list.append(tk.Checkbutton(
      window,
      text = "Keep",
      variable = enable[i],
      onvalue=1,
      offvalue=0,
      ))
    for i in range(len(chkBox_list)):
      chkBox_list[i].grid(
          row = 1,
          column = i)

btn_roll_dice = tk.Button(text="Roll the Dice!",command=roll_dice)
btn_roll_dice.grid(row=2, column=2)

lbl_chance = tk.Label(text="Chance: ")
lbl_chance.grid(row=2, column=4)

lbl_threes = tk.Label(text="Three of a kind: ")
lbl_threes.grid(row=3, column=5)

lbl_fours = tk.Label(text="Four of a kind: ")
lbl_fours.grid(row=4, column=5)

lbl_fulls = tk.Label(text="Full house: ")
lbl_fulls.grid(row=5, column=5)

lbl_sm = tk.Label(text="Small straight: ")
lbl_sm.grid(row=6, column=5)

lbl_lg = tk.Label(text="Small straight: ")
lbl_lg.grid(row=7, column=5)

lbl_yahtzee = tk.Label(text="Yahtzee!: ")
lbl_yahtzee.grid(row=8, column=5)

# Create the labels for singles
lbl_singles = [tk.Label(text= str(i+1) + "'s: ") for i in range(6)]
for i in range(6):
    lbl_singles[i].grid(row=3+i, column=4)


tk.mainloop()
