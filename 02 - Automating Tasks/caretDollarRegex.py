import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello, world.'))
print(beginsWithHello.search('He said hello'))
print('\n')

endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Forty two'))
print('\n')

wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('123456789'))
print(wholeStringIsNum.search('12345xyz678'))
print(wholeStringIsNum.search('12345   678'))