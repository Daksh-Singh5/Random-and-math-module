import random
num = 0
randomnum = random.randint(1,100)
while num != randomnum: 
    num = int(input("pick a number from 1 to 100: "))
    if num < randomnum:
        print("too small")
        continue
    elif num > randomnum:
        print("too big")
        continue
    else:
        print("you win")
