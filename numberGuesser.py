import random
a,b = 1,100
num = random.randint(a,b)
n = int(input(f"Guess the number between {a} to {b}: "))
attempts = 0
while True:
    attempts+=1
    if n == num:
        print(f"===Correct its {n}! CONGRATULATIONS!===")
        print(f"Number of Attempts taken: {attempts}")
        break
    elif n>num:
        n = int(input("Nope.Try a smaller number: "))
    
    else:
        n = int(input("Nope.Try a bigger number: "))