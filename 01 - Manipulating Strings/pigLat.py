#English to Pig Latin
print('Enter the english message to translate into Pig Latin.')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u')

pigLatin = [] #A list of words in PigLatin.
for word in message.split():
    #Seperate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    #Seperate the non-letters are the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    #Remember if the words were in uppercase or or title case
    wasUpper = word.upper()
    wasTitle = word.title()

    word = word.lower() #Make the word lowercase for translation

    #Seperate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    #Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    #Set the word back to upper or title case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    #Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

#Join all the words back together into a single string:
print(' '.join(pigLatin))
