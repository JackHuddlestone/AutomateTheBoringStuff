#Practicing with pyinputplus
import pyinputplus as pyip

while True:
    response = pyip.inputYesNo(prompt='Want to know how to keep an idiot busy for hours?\n')
    if response == 'no':
        break

print('Thank you, have a nice day.')
