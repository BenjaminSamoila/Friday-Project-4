# Define a dictionary with trivia questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "Who wrote Romeo and Juliet?": "William Shakespeare",
    "What is the largest mammal?": "Blue whale",
    "How many continents are there?": "7",
    "What year did the Titanic sink?": "1912"
}

# Iterate over the dictionary to display questions and check answers
for question, answer in questions.items():
    print(question)
    user_answer = input("Your answer: ")
    
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {answer}\n")