#jogo do pedra, papel e tesoura contra o pc

import random

print("-Rock, Paper or Scissors game-")

hand = ['rock', 'paper', 'scissors']

hum_vit = 0
com_vit = 0

cont = 1

while cont < 4:
    print(f"\nChoose rock, paper or scissors - round({cont})\n")

    computer_hand = random.choice(hand)

    human_hand = ''

    while human_hand not in hand:
        try:
            human_hand = input("Your choice: ")
            choice = hand.index(human_hand)
        except ValueError:
            print("Try a valid choice")


    if human_hand == 'rock' and computer_hand == 'paper':
        print("You lost this round: ")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        com_vit += 1
        cont += 1
    elif human_hand == 'rock' and computer_hand == 'scissors':
        print("You won this round: ")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        hum_vit += 1
        cont += 1
    elif human_hand == 'paper' and computer_hand == 'rock':
        print("You won this round: ")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        hum_vit += 1
        cont += 1
    elif human_hand == 'paper' and computer_hand == 'scissors':
        print("You lost this round: ")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        com_vit += 1
        cont += 1
    elif human_hand == 'scissors' and computer_hand == 'rock':
        print("You lost this round: ")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        com_vit += 1
        cont += 1
    elif human_hand == 'scissors' and computer_hand == 'paper':
        print("You won this round: ")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        hum_vit += 1
        cont += 1
    else:
        print("\n Draw \n")
        print(f"You hand: {human_hand}")
        print(f"Computer hand: {computer_hand}")
        continue

print("-Gamer over!-\n")

if hum_vit > com_vit:
    print("-You win-")
    print(f"Wins: {hum_vit}")
    print(f"Losts: {com_vit}")
else:
    print("-You lose-")
    print(f"Wins: {hum_vit}")
    print(f"Losts: {com_vit}")

