quiz_questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Paris", "London", "Berlin", "Rome"],
        'correct_answer': "Paris"
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'options': ["Venus", "Mars", "Jupiter", "Saturn"],
        'correct_answer': "Mars"
    },
    {
        'question': "What is the largest mammal in the world?",
        'options': ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        'correct_answer': "Blue Whale"
    },
    {
        'question': "Which gas do plants absorb from the atmosphere?",
        'options': ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        'correct_answer': "Carbon Dioxide"
    },
    {
        'question': "Who painted the Mona Lisa?",
        'options': ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
        'correct_answer': "Leonardo da Vinci"
    },
    {
        'question': "Which country is famous for the Taj Mahal?",
        'options': ["India", "Egypt", "Greece", "China"],
        'correct_answer': "India"
    },
    {
        'question': "In which year did Christopher Columbus discover America?",
        'options': ["1492", "1620", "1776", "1832"],
        'correct_answer': "1492"
    },
    {
        'question': "What is the chemical symbol for gold?",
        'options': ["Au", "Ag", "Fe", "Cu"],
        'correct_answer': "Au"
    },
    {
        'question': "Who wrote the play 'Romeo and Juliet'?",
        'options': ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        'correct_answer': "William Shakespeare"
    },
    {
        'question': "What is the largest ocean in the world?",
        'options': ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        'correct_answer': "Pacific Ocean"
    }
]

user_score = 0

print("Welcome to the Quiz Game!")
print("Answer each question to the best of your knowledge.")

for idx, question_data in enumerate(quiz_questions):
    print(f"\nQuestion {idx + 1}: {question_data['question']}")
    for i, option in enumerate(question_data['options']):
        print(f"{i + 1}. {option}")
    
    user_answer = input("Your answer: ")

    if user_answer.lower() == question_data['correct_answer'].lower():
        user_score += 1
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is: {question_data['correct_answer']}")

print("\nQuiz completed!")
print(f"Your final score: {user_score} out of {len(quiz_questions)}")

if user_score == len(quiz_questions):
    print("Congratulations! You got a perfect score!")
elif user_score >= len(quiz_questions) / 2:
    print("Good job! You did well.")
else:
    print("Keep practicing to improve your score.")
