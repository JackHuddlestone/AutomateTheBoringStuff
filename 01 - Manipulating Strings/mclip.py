#! python3
#mclip.py - A multi-clipboard program.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'decline': """Unfortunately I must decline."""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python3 mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #First command line argument is the phrase.

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to keyboard.')
else:
    print('There is no text for ' + keyphrase)
