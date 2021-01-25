#Multiplication quiz written with pyip
import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0
print('== Python Multiplication Quiz ==\n')
for question in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = (f'Question #{question + 1} : {num1} x {num2} = ')
    
    try:
        # Right answers are handled by the allowRegexs.
        # Wrong answers are handled by the blockRegexs.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=['.*', 'Incorrect!'], timeout=8, limit=3)
    
    # Spent more than 8 seconds on an answer.
    except pyip.TimeoutException:
        print('Out of time!')

    # Too many incorrect attempts.
    except pyip.RetryLimitException:
        print('Out of tries!')

    # Correct answer.
    else:
        print('Correct Answer!')
        correctAnswers += 1

    # Provide the user with one second to see the result.
    time.sleep(1)
        
print('\n== Thanks for playing ==')
if correctAnswers == numberOfQuestions:
    print(f'Congratulations! You scored all the questions correct')

else:
    print(f'Thanks for playing. You scored {correctAnswers}/{numberOfQuestions}.')