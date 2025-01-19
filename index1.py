import random

user=input("Pick from rock paper scissors: ")
array = ["Rock","Paper","scissors"]

user=user.lower()

game = random.choice(array)
print(game)

print("you: ",user)
print("enemy: ",game)

if user=="rock" and game == "rock":
    print("Its a tie both are rocks")
elif user=="paper" and game == "paper":
    print("Its a tie both are paper")
elif user=="scissors" and game == "scissors":
    print("Its a tie both are scissors")
elif user=="scissors" and game == "paper":
    print("scissors cuts paper so user wins")
elif user=="paper" and game == "scissors":
    print("scissors cuts paper so enemy wins")
elif user=="rock" and game == "Paper":
    print("paper suffocates rock so enemy wins")
elif user=="Paper" and game == "rock":
    print("paper suffocates rock so user wins")
elif user=="scissors" and game == "paper":
    print("scissors cut paper so user wins")
elif user=="paper" and game == "scissors":
    print("scissors cut paper so user wins")