import random

def helper(c,u):
    if c==u:
        print("Its a Draw!")
    elif (c==1 and u==2) or (c==2 and u==3) or (c==3 and u==1):
        print("You Won!")
    else:
        print("You Lose!")
        

if __name__ == "__main__":
    print("NOTE: 1:Rock, 2:Paper, 3:Scissors")
    user_input = int(input("Enter any number: "))
    comp_input = random.randint(1,3)
    choices = {1:"Rock",
               2:"Paper",
               3:"Scissors"}
    print("---------------------------------")
    print(f"Your Choice: {choices[user_input].upper()}")
    print(f"Computer's Choice: {choices[comp_input].upper()}")
    print("---------------------------------")
    helper(comp_input, user_input)