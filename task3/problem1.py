
import random
def pick_winner(names):
    if not names:
        return "No names entered!"

    winner = random.choice(names)
    return f" the winner is : {winner} congratulation!"
names = input("Enter names separated by space: ").split()

print(pick_winner(names))