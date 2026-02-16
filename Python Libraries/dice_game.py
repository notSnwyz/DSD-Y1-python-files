import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    return die1, die2, total


def play_game():
    lives = 3
    rounds_played = 0
    wins = 0

    print("Welcome to the Dice Game!")
    print("Roll a total of 7 or 11 to win.")
    print("You have 3 lives.\n")

    while lives > 0:
        input("Press Enter to roll the dice...")

        die1, die2, total = roll_dice()
        rounds_played += 1

        print(f"You rolled: {die1} and {die2}")
        print(f"Total score: {total}")

        if total == 7 or total == 11:
            print("You Win!\n")
            wins += 1
        else:
            lives -= 1
            print("Try Again")
            print(f"Lives remaining: {lives}\n")

    win_percentage = (wins / rounds_played) * 100 if rounds_played > 0 else 0

    print("Game Over!")
    print(f"Rounds Played: {rounds_played}")
    print(f"Wins: {wins}")
    print(f"Win Percentage: {win_percentage:.2f}%")

if __name__ == "__main__":
    play_game()
