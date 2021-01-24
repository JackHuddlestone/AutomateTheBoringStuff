import re
import pyperclip

# Get body of text from the clipboard.

try: 
    text = pyperclip.paste()
    print('SUCCESS: Text copied from clipboard.')
except (SyntaxError, TypeError):
    print('ERROR: No text on your clipboard.')
    

# Prompt for the character that requires stripping.
print('What character needs stripping?')
stripCharacter = input('Leave empty to remove whitespace -> ')

# Function which removes the character.
def stripText(input, character):
    if stripCharacter == '':
        regexStrip = re.compile(r'^\s*|\s*$')
        stripped = regexStrip.sub('', text)
        pyperclip.copy(stripped)
        print('SUCCESS: Stripped text copied to clipboard.')
        
    else:
        regexStrip = re.compile(rf'{stripCharacter}', re.IGNORECASE)
        stripped = regexStrip.sub('', text)
        pyperclip.copy(stripped)
        print('SUCCESS: Stripped text copied to clipboard.')

# Call the function
stripText(text, stripCharacter)

