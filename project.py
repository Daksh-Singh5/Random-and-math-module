import random
import math
num = random.randint(1,100)
num2 = random.randint(1,100)
opperter = ["+","-","x","/"]
choice = random.choice(opperter)
if choice == "+":
    ans = num+num2
elif choice == "-":
    ans = num-num2
elif choice == "x":
    ans = num*num2
elif choice == "/":
    while num%num2==0:
        num = random.randint(1,100)
        num2 = random.randint(1,100)      
    ans = num/num2
print(num,choice,num2)
ans2 = int(input("Enter the answer for this: "))
while ans != ans2:
    if ans == ans2:
        print("Wow u did it")
        continue
    else:
        print("try again")
        ans2 = int(input("Enter the answer for this: "))