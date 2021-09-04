round = 1   #global variable
import random  #import random module
def stone_paper():
    count1 = 0
    count2 = 0
    for i in range(3):
        global round
        computer_choice = random.choice(["stone", "paper", "sessiors"])
        choice = input(f"Round-{round} enter your choice - ")
        if choice == computer_choice:
            print("Draw")
            round += 1
        elif choice == "paper" and computer_choice == "stone" or choice == "stone" and computer_choice == "sessiors" or choice == "sessiors" and computer_choice == "paper":
            print("you win this round")
            count2 = count2 + 1
            round += 1
        else:
            print("you lose this round")
            count1 = count1 + 1
            round += 1
    if count2>count1:
        return "congo you win"
    elif count2==count1:
        return "game draw"
    else:
        return "sorry you lose"


if __name__ == '__main__':
    print("welcome to stone paper sessiors, you won on loss on the basis of best of three \n 1-> stone \n 2-> paper \n 3-> sessiors \n choose between any three of them")
    print(stone_paper())
