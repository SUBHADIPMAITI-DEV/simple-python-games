import time
import random

class QuizGame:
    def __init__(self):
        self.categories = [
            "Sports",
            "Geography",
            "History",
            "Trivia quizzes",
            "Animal quizzes",
            "General knowledge"
        ]

        self.questions = {
            "Sports": [
                {
                    "question": "Which country won the FIFA World Cup in 2018?",
                    "options": ["A. France", "B. Brazil", "C. Germany", "D. Argentina"],
                    "correct_answer": "A"
                },
                {
                    "question": "In which sport would you perform a slam dunk?",
                    "options": ["A. Soccer", "B. Basketball", "C. Tennis", "D. Golf"],
                    "correct_answer": "B"
                },
                # Add more sports-related questions
            ],
            "Geography": [
                {
                    "question": "What is the capital of Australia?",
                    "options": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"],
                    "correct_answer": "B"
                },
                {
                    "question": "Which river is the longest in the world?",
                    "options": ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"],
                    "correct_answer": "A"
                },
                # Add more geography-related questions
            ],
            # Add more categories and questions as needed
        }

        self.score = 0
        self.timer_duration = 10  # Time to answer each question in seconds

    def shuffle_options(self, options):
        random.shuffle(options)

    def display_categories(self):
        print("Choose a category:")
        for i, category in enumerate(self.categories, start=1):
            print(f"{i}. {category}")
        category_choice = int(input("Enter the number of your chosen category: "))
        return self.categories[category_choice - 1]

    def display_question(self, category, question):
        print(f"\n{category} Question:")
        print(question["question"])
        for option in question["options"]:
            print(option)

    def start_game(self):
        print("Welcome to the Quiz Game!")
        selected_category = self.display_categories()

        for _ in range(5):  # Let's ask 5 questions per category
            question = random.choice(self.questions[selected_category])
            self.shuffle_options(question["options"])
            self.display_question(selected_category, question)

            start_time = time.time()
            user_answer = input("Your answer: ").upper()

            if time.time() - start_time > self.timer_duration:
                print("Time's up! You took too long to answer.")
            elif user_answer == question["correct_answer"]:
                print("Correct! +2 points")
                self.score += 2
            else:
                print("Incorrect. -1 point")

            time.sleep(1)

        print(f"\nQuiz completed! Your final score is: {self.score}")

if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.start_game()
