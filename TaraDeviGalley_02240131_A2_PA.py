import random

class GuessNumberGame:
    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.secret_number = random.randint(self.lower_bound, self.upper_bound)
        self.max_attempts = 10
        self.score = 0

    def play(self):
        print(f"I'm thinking of a number between {self.lower_bound} and {self.upper_bound}.")
        attempts = 0
        while attempts < self.max_attempts:
            try:
                guess = int(input(f"Attempt {attempts + 1}/{self.max_attempts}. Enter your guess: "))
                if not self.lower_bound <= guess <= self.upper_bound:
                    print(f"Please enter a number between {self.lower_bound} and {self.upper_bound}.")
                    continue
                attempts += 1
                if guess < self.secret_number:
                    print("Too low!")
                elif guess > self.secret_number:
                    print("Too high!")
                else:
                    self.score = max(0, 100 - (attempts - 1) * 10)
                    print(f"Congratulations! You guessed the number {self.secret_number} in {attempts} attempts. Your score is {self.score}.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print(f"Your score for this game is: {self.score}")
        return self.score


class RockPaperScissorsGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds = 3

    def play(self):
        print("Let's play Rock, Paper, Scissors!")
        for round_num in range(self.rounds):
            while True:
                user_choice = input(f"Round {round_num + 1}/{self.rounds}. Choose rock, paper, or scissors: ").lower()
                if user_choice in self.choices:
                    break
                print("Invalid choice.")
            computer_choice = random.choice(self.choices)
            print(f"Computer chose: {computer_choice}.")
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("You win this round!")
                self.user_wins += 1
            else:
                print("Computer wins this round!")
                self.computer_wins += 1

        print("Game over!")
        print(f"Your wins: {self.user_wins}, Computer wins: {self.computer_wins}")
        if self.user_wins > self.computer_wins:
            print("You won the game!")
        elif self.user_wins < self.computer_wins:
            print("Computer won the game!")
        else:
            print("It's a tie game!")
        return self.user_wins


class TriviaPursuitGame:
    def __init__(self):
        self.categories = {
            "Science": [
                {"question": "What is the chemical symbol for water?", "options": ["CO2", "H2O", "Au", "NaCl"], "answer": "H2O"},
                {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Sun", "Jupiter", "Stars"], "answer": "Jupiter"},
                {"question": "What is the speed of light?", "options": ["300,000 km/s", "150,000 km/s", "1,000,000 km/s", "500,000 km/s"], "answer": "300,000 km/s"},
            ],
            "History": [
                {"question": "When did Zhabdrung come to Bhutan?", "options": ["1010", "1666", "1616", "1660"], "answer": "1616"},
                {"question": "In which year did World War II end?", "options": ["1942", "1945", "1948", "1950"], "answer": "1945"},
                {"question": "What is the name of the animal on the Bhutanese flag?", "options": ["Tara", "btsan(Tiger)", "Dbe Bsnyen", "Druk(Dragon)"], "answer": "Druk(Dragon)"},
            ],
            "Geography": [
                {"question": "What is the capital city of Bhutan?", "options": ["Thimphu", "Gelephu", "Paro", "Phuntsholing"], "answer": "Thimphu"},
                {"question": "What is the highest peak in Bhutan?", "options": ["Kula Kangri", "Jomolhari", "Kangchendzonga", "Gangkhar Puensum"], "answer": "Gangkhar Puensum"},
                {"question": "What is the main religion in Bhutan?", "options": ["Hinduism", "Buddhism", "Christianity", "Islam"], "answer": "Buddhism"},
            ]
        }
        self.score = 0

    def play(self):
        print("Welcome to Trivia Pursuit Quiz Game!")
        for category, questions in self.categories.items():
            print(f"\nCategory: {category}")
            for q in questions:
                print(f"\nQuestion: {q['question']}")
                for i, opt in enumerate(q['options']):
                    print(f"{i + 1}. {opt}")
                while True:
                    try:
                        answer = int(input("Enter your answer number: "))
                        if 1 <= answer <= len(q["options"]):
                            break
                        else:
                            print("Invalid choice.")
                    except ValueError:
                        print("Invalid input.")
                if q["options"][answer - 1] == q["answer"]:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer was {q['answer']}.")
        total_questions = sum(len(qs) for qs in self.categories.values())
        print(f"\nYour final score: {self.score}/{total_questions}")
        return self.score


class PokemonCardBinderManager:
    def play(self):
        print("Welcome to Pokemon Card Binder Manager!")
        print("This functionality will be implemented in Part B.")
        return 0


class GameCenter:
    def __init__(self):
        self.scores = []

    def show_menu(self):
        print("\nSelect a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Trivia Pursuit Quiz Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Overall Score")
        print("0. Exit")

    def check_overall_score(self):
        if not self.scores:
            print("No games played yet. Overall score: 0")
            return 0
        total = sum(self.scores)
        print(f"Overall score from all games: {total}")
        return total

    def run(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    game = GuessNumberGame()
                    self.scores.append(game.play())
                elif choice == 2:
                    game = RockPaperScissorsGame()
                    self.scores.append(game.play())
                elif choice == 3:
                    game = TriviaPursuitGame()
                    self.scores.append(game.play())
                elif choice == 4:
                    game = PokemonCardBinderManager()
                    self.scores.append(game.play())
                elif choice == 5:
                    self.check_overall_score()
                elif choice == 0:
                    print("Exiting the program.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 0 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    GameCenter().run()
