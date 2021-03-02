import random #importing the random library to use for setting the initial guess numbers randomly.

numbers = [] #initialize the list of random numbers to guess from.

for settingNumbers in random.sample(range(21), 5): #for loop to append 5 random numbers into the guess list.
    numbers.append(settingNumbers)


while True: #infinite loop.
    print("\nType 'q' to quit or, type 'a' to quit and see the correct guesses") 
    userInput = input("Guess a number between 0 and 20, there are 5 correct answers: ") #collect user input.

    if userInput == "q": #press q to quit.
        print("\nGoodbye.")
        break

    elif userInput == "a": #press a to quit and get the answers.
        print("Give up? Here are the correct guesses.")
        print(numbers)
        break

    elif int(userInput) > 20 or int(userInput) < 0: #to prevent the user guessing out of range.
        print("Please guess between the numbers 0 throught 20, inclusive.")
        continue

    try: #try-except blocks to handle the user entering a string.
        if int(userInput) in numbers: #correct guess removes that number from the list.
            numbers.remove(int(userInput))
            print("You guessed " + userInput + " which is a number in the list of correct"
                   + " guesses, well done!")

            if len(numbers) > 0: #if there are still numbers left to guess, the program continues.
                print("\nCan you guess the rest?")
                continue

            elif len(numbers) == 0: #if all numbers are guessed, the program finishes.
                print("\nCongratulations, you guessed them all!")
                break
    except ValueError:
        print("\nPlease enter an integer as a guess, or press q to quit.")

    else: #to let the user know that they have guessed incorrectly.
        print("That was an incorrect guess! Please try again.")
        
    
    






