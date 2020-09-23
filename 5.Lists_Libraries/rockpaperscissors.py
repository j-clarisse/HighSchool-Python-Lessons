import random
print("Let's play scissors/paper/rock!")

options = ["scissors","paper","rock"]
cpu = random.choice(options)

player = input("What do you want to play (scissors/paper/rock?) ")

player = player.lower()
if (player != "scissors" and player != "paper" and player != "rock"):
  print("Invalid move.")

if (cpu == player):
  print("CPU:",cpu,"vs Player:",player)
  print("TIE!")
else:
  print("CPU:",cpu,"vs Player:",player)

if (cpu == "scissors"):
  if (player == "rock"):
    print("YOU win!")
  else:
    print("CPU wins :(")
if (cpu == "paper"):
  if (player == "scissors"):
    print("YOU win!")
  else:
    print("CPU wins :(")
if (cpu == "rock"):
  if (player == "paper"):
    print("YOU win!")
  else:
    print("CPU wins :(")
