#Importing Stuff
import random
from random import randint
from ascii_logo import logo

#Player Attack DMGS
awp_dmg = "50"
sniper_dmg = "100"
grenade_dmg = "30"

#Player Characteristics
character = "(　-_･)"
your_hp = 100

#Level 1 Characteristics
enemy1 = "👽"
level1_enemy_hp = 100

#Level 2 Characteristics
level2_enemy_hp = 200
enemy2 = "👾"

#Level 3 Characteristics
level3_enemy_hp = 300
enemy3 = "🤖"

#Level 4 Characteristics
level4_enemy_hp = 400
enemy4 = "👺"

#Boss Level Characteristics
boss = "ᕙ〳 ರ ︿ ರೃ 〵ᕗ" 
boss_hp = 500

#Win/Lose Functions
def victory(character):
  print(character + "︻デ═一 ▸  BOOM! You won!")

def loss(character):
  print(character + " you lose")

def check_win1():
  if your_hp <= 0:
    loss("(X_X)")
  elif your_hp <= 100 or your_hp >= 100:
    print("Battle is still going on...")
  else:
    victory("(　-_･)")

def check_win2():
  if your_hp <= 0:
    loss("(X_X)")
  elif your_hp <= 150 or your_hp >= 150:
    print("Battle is still going on...")
  else:
    victory("(　-_･)")

def check_win3():
  if your_hp <= 0:
    loss("(X_X)")
  elif your_hp <= 200 or your_hp >= 200:
    print("Battle is still going on...")
  else:
    victory("(　-_･)")

def check_win4():
  if your_hp <= 0:
    loss("(X_X)")
  elif your_hp <= 250 or your_hp >= 250:
    print("Battle is still going on...")
  else:
    victory("(　-_･)")

def check_win_boss():
  if your_hp <= 0:
    loss("(X_X)")
  elif your_hp <= 300 or your_hp >= 300:
    print("Battle is still going on...")
  else:
    victory("(　-_･)")

#Player Attack Functions
def AWP_attack():
  print(character + "︻デ═一 ----------------> KAPOW!\nDMG Done: " + awp_dmg)

def SNIPER_attack():
  print(character + "▄︻̷̿┻̿═━一 ------------------------------> OOF!\nDMG Done: " + sniper_dmg)

def GRENADE_attack():
  print(character + "-----------💣... 💥💥💥 Well, that wrecked me!\nDMG Done: " + grenade_dmg)

#Level 1 Attack Functions
print(logo)

