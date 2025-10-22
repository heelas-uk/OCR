print("Welcome to the number game")
import random as r
total = r.randint(10, 30)
print(f"Starting with {total} tokens.")

while total > 0:
    # AI move: misère rule (last token loses). Try to leave 1 mod 4.
    p2 = (total - 1) % 4
    if p2 == 0:
        p2 = 12
    p2 = min(p2, 3, total)
    total -= p2
    print(f"AI took {p2} tokens; remaining: {total}")
    if total == 0:
        print("AI took the last token. Player wins.")
        break

    # Player move: keep asking until a valid move
    while True:
        try:
            p1 = int(input(f"Player, take 1-3 tokens (remaining {total}): "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if 1 <= p1 <= 3 and p1 <= total:
            break
        print("Invalid move. Take 1-3 tokens and not more than remaining.")
    total -= p1
    if total == 0:
        print("You took the last token. AI wins.")
        break
