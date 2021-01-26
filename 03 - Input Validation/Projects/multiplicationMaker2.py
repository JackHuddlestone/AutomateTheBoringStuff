#write the multiplication quiz without pyinputplus.
import random, time # import dependencies

questions = 2 # insert number of questions in quiz

# function to perform multiplication
def multiplicationQuestion(number):
    tick = time.perf_counter() #begin counting for the 8 second limit
  
    num1, num2 = random.randint(0,9), random.randint(0,9)  # generate 2 random numbers
    correct_answer = num1 * num2 # performs the sum to get the correct answer

    print(f'\nQuestion #{number + 1} : {num1} x {num2} = ') # prints the question to the screen
    
    attempts = 1 # question attempts
    while (attempts <= 3): # 3 attempts at a question
        try:
            answer = int(input('Answer -> ')) # prompts for users answer

        except (ValueError):
            print('Incorrect, answer needs to be a number.') # if user enters anything but integer capture exception.
            attempts += 1

        try:
            if answer == correct_answer: # if correct answer
                tock = time.perf_counter() # finish counting time
                time_taken = (f'{tock - tick:0.2f}') # work out the time taken to answer correctly
                if float(time_taken) >= 8.0: # if answer correct and takes more than 8 seconds
                    print(f'Correct answer, but out of time! You took {time_taken} seconds to answer.')
                    break

                else: # if answer correct and taken less than 8 seconds.
                    print(f'Correct! You took {time_taken} seconds to answer.')
                    return 1 # returns one for correct answer tally

            elif answer != correct_answer and attempts < 2: # if answer not correct and less than two attempts
                print('Incorrect, try again!')
                attempts += 1 # adds one attempt

            elif answer != correct_answer and attempts == 2: # if answer not correct and on final attempt
                print('Incorrect, last attempt!')
                attempts += 1 # adds one attempt
            
            else: # if user does not get question right after three attempts.
                print('Incorrect, skipping question!')
                break

        except UnboundLocalError: # Catches exception from incorrect formatted input
            continue
    
correct = 0 # number of correct answers
for question in range(questions): # initiates the quiz
    if multiplicationQuestion(question) == 1: #if returns correct question (1) then add 1 to correct variable
        correct += 1
    time.sleep(1) # sleep for a second and let them see result

print(f'\nYOUR SCORE - {correct}/{questions}') # print final score