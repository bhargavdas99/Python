import getpass

def game(attempt):
    num = getpass.getpass("Enter your SECRET number. (Number will be invisible while typing): ")
    s = ["X" for _ in num]
    print("====Guess numbers and replace X to find the full number====")
    num_of_x = len(num)
    while True:
        attempt += 1
        tmp = " ".join(s)
        print(f"Current State: {tmp} || You got {len(num) - num_of_x} digits correct so far.")
        inp = input("Guess the number: ")

        if len(inp) != len(num):
            print(f"Your guess should have length {len(num)}")
            attempt -= 1
            continue
        for i in range(len(num)):
            if num[i] == inp[i] and s[i] == "X":
                s[i] = num[i]
                num_of_x -= 1
        
        if "X" not in s:
            print(f"Congrats!! You guessed the number: {num}")
            print(f"Number of attempts taken: {attempt}")
            break
        
    return attempt

# Player 2 guesses. Player 1 chooses a number
print("Player 1, please choose a number for Player 2 to guess.")
p2_score = game(0)
print("Player 2, please choose a number for Player 1 to guess.")
# Player 1 guesses. Player 2 chooses a number
p1_score = game(0)

print("=== FINAL SCORE: Player1:{p1_score} || Player2:{p2_score} ===")
if p2_score < p1_score:
    print("Player 2 wins!")
elif p1_score < p2_score:
    print("Player 1 wins!")
else:
    print("It's a draw!")
