import random

# Define questions and their answer sets
questions = [
    {"question": "What is 1+2?", "answers": ["3", "4", "5", "6"], "correct": "3"},
    {"question": "What sign is used to multiply?", "answers": ["x", "/", "+", "-"], "correct": "x"},
    {"question": "What remains the same after differentiation?", "answers": ["e^x", "x", "x^2", "y"], "correct": "e^x"}
]

def main():
    score = 0
    random.shuffle(questions)  # Shuffle questions for a random order
    
    for question_data in questions:
        print(question_data["question"])
        
        # Randomize answer choices each time
        answers = question_data["answers"]
        random.shuffle(answers)
        
        # Display the answer options
        for answer in answers:
            print(answer)
        
        user_answer = input("Your answer (Key in the full value/sign): ").strip()
        
        # Check if the answer is correct
        if user_answer == question_data["correct"]:
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect!\n")
    
    print(f"Your final score is {score} out of {len(questions)}!")

print("Welcome to the Math Quiz Game!")

def math_quiz_game():
    while True:
        start = input("Type 'Start' to begin or 'Exit' to quit: ").strip().capitalize()

        if start == "Start":
            main()
        elif start == "Exit":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input, please try again.")

math_quiz_game()
