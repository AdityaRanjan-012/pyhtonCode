import sys
import random

def game_tree(n, depth=0, alpha=float('-inf'), beta=float('inf')):
    if n <= 0 or depth == 0:
        return (0, 0) if n % 2 == 0 else (1, 0)

    if depth == 10:  # Maximum depth for pruning
        return (0, 0)

    best_score = float('-inf')
    for i in range(1, 4):
        next_n = n - i
        if next_n < 0:
            continue
        score, _ = game_tree(next_n, depth + 1, alpha, beta)
        if depth % 2 == 0:
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
        else:
            best_score = min(best_score, score)
            beta = min(beta, best_score)

        if beta <= alpha:
            break

    return (best_score, depth)

def ai_vs_human(n):
    ai_score, _ = game_tree(n, 0)
    if ai_score == 1:
        print("AI wins!")
    elif ai_score == 0:
        print("Draw!")
    else:
        print("Human wins!")

if __name__ == "__main__":

    n = int(input("take the n as input: "))
    toss = random.randint(0, 1)
    if toss == 0:
        print("AI goes first.")
        ai_vs_human(n)
    else:
        print("Human goes first.")
        ai_vs_human(n)
