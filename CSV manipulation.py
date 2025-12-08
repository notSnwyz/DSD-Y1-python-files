import csv

FILENAME = "scores.csv"


def add_score(username, score):
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])


def get_all_scores():
    """Read all scores from file and return list of (user, score)."""
    scores = []
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    username = row[0]
                    try:
                        score = int(row[1])
                        scores.append((username, score))
                    except ValueError:
                        pass  # ignore invalid lines
    except FileNotFoundError:
        pass
    return scores


def show_scores():
    scores = get_all_scores()
    for username, score in scores:
        print(f"User: {username}, Score: {score}")


def show_leaderboard():
    scores = get_all_scores()

    # Filter: only scores > 50
    filtered = [entry for entry in scores if entry[1] > 50]

    if not filtered:
        print("\nNo scores above 50 found.")
        return

    # Sort descending
    filtered.sort(key=lambda x: x[1], reverse=True)

    print("\n=== Leaderboard (Scores > 50) ===")
    for i, (user, score) in enumerate(filtered, start=1):
        print(f"{i}. {user} — {score}")

    # Stats
    total_attempts = len(filtered)
    average_score = sum(score for _, score in filtered) / total_attempts

    print("\n--- Stats ---")
    print(f"Attempts counted: {total_attempts}")
    print(f"Average score: {average_score:.2f}")

def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Show leaderboard")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            show_leaderboard()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()