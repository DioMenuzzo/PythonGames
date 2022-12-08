#Function to create a new game.
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    #Showing the Questions
    for key in questions:
        print("-"*100)
        print(str(question_num) + ". " + key)
        for i in options[question_num-1]:                                       #question_num = 1 and dictionary starts at 0
            print(i)

        #Player input the answer
        guess = input("Enter A, B, C or D: ")
        guess = guess.upper()                                                   #Case sensitive
        guesses.append(guess)                                                   #Add the guess to the guesses list

        #Checking the answer:
        correct_guesses += check_answer(questions.get(key), guess)              #Add 1 if correct and add 0 if wrong
        question_num += 1                                                       #Go to the next question

    display_score(correct_guesses, guesses)

#Function to check the answers.
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

#Function to display the Player's score
def display_score(correct_guesses, guesses):
    print("-"*100)
    print("\nRESULTS")

    print("Answers", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%\n")

#Function to play again
def play_again():
    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    
    else:
        return False

#Dictionary with all the questions.
questions = {
"What is the mass per unit volume of material called? ": "C",
"What is major element making up the sun? ": "D",
"Which scientist explained the concepts of gravity and motion? ": "A",
"What is the typical heart rate in a healthy adult?": "A",
"Food energy is expressed in what form? ": "D",
"The Haiku, a three-line poem that utilizes images from nature, originated in which country?" : "B",
"“Crime and Punishment”, “Anna Karenina,” and “Dr. Zhivago” all belong to which kind of literature? ": "C",
"Which German political leader was known as the “Iron Chancellor”? ": "B",
"Focaccia al Rosmarino is a food item of what type of cuisine? ": "D",
"Which famous battle ended the Napoleonic Wars? ": "A"
}

#2D list for the answers.
options = [
["A. Area", "B. Weight", "C. Density", "D. Solid"],
["A. Oxigen", "B. Carbon", "C. Helium", "D. Hydrogen"],
["A. Isaac Newton", "B. Galileo Galilei", "C. Nicolaus Copernicus", "D. Carl Friedrich Gauss "],
["A. 60-80 bpm", "B. 80-100 bpm", "C. 100-120 bpm", "D. 120-140 bpm"],
["A. volt", "B. kilogram", "C. coulomb", "D. calorie"],
["A. China", "B. Japan", "C. South Korea", "D. Mongolia"],
["A. Hungarian", "B. German", "C. Russian", "D. French"],
["A. Albrecht von Roon", "B. Otto von Bismark", "C. Helmuth von Moltke", "D. Leo von Caprivi"],
["A. French", "B. Spanish", "C. Turkish", "D. Italian"],
["A. Waterloo", "B. The Hundred Years' War", "C. Wars of the Roses", "D. Crusades"]
]

new_game()

while play_again():
    new_game()

print("Thanks for playing! Bye, Bye!")