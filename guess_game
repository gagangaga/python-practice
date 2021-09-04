c= 1
def gusse_game(num,item):
    if num==item:
        global c
        print("no of attepmpts",c)
        return "congo you won"
    else:
        c = c+1
        print("wrong choice")
        print("number of choice left",11-c)
        while c<11:
            if num<item:
                print("HINT - choose greater number than",num)
            else:
                print("HINT - choose lesser number than",num)
            newnum = int(input("enter the next choice"))
            return gusse_game(newnum,item)
        return ("you lose")




if __name__ == '__main__':
    import random
    print("welcome to my guessdigit game, rules are -" '\n' "1-> you have total of 10 choices" '\n' "2-> if you enter"
          "the wrong answer, then we gave you some hints")
    item = random.randint(10,99)
    num = int(input("enter your choice"))
    print(gusse_game(num,item))
