#!/sbin/python3

import tkinter as tk
import random
import playsound
from scoring_functions import *

window = tk.Tk()
window.title("Yahtzee! World")
window.geometry("700x300")

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
  lbl_chance['text'] = "Chance: "+str(chance(dice_rolls))
  for i in range(6):
    lbl_numbers[i]['text'] = str(i+1) + "'s: " + str(singles(dice_rolls,i+1))

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

# Create the labels for 1's, 2's, 3's, etc.
lbl_numbers = []
for i in range(6):
  lbl_numbers.append(tk.Label(text= str(i+1) + "'s: "))
  lbl_numbers[i].grid(row=3+i, column=4)

tk.mainloop()
