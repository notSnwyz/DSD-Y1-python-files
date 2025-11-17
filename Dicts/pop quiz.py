score = 0

quiz = {
    "What is the name of the capital of Romania?" : "Bucharest",
    "Who painted the Mona Lisa?" : "Leonardo da Vinci",
    "What is the largets ocean on Earth?" : "The Pacific Ocean",
    "What is the chemical symbol for gold?" : "Au",
    "Who was the lead singer of Nirvana?" : "Kurt Cobain",
    "What was the first feature-length movie made by Pixar?" : "Toy Story",
    "What is the hottest planet in out solar system?" : "Venus",
    "What is the largest organ in the human body?" : "The skin",
    "Which scientist is credited with the laws of motion and universal gravitation?" : "Sir Isaac Newton",
    "What does the acronym URL stand for in the context of the internet?" : "Uniform Resource Locator"
}

for question, correctAnswer in quiz.items():
    userAnswer = input(question + " ")
    if userAnswer.lower() == correctAnswer.lower():
        score += 1
        print("Correct")
    else:
        print("Incorrect")    

print(f"Your total score was {score}/10")
    