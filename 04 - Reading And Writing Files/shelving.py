import shelve
shelfFile = shelve.open('data')
dogs = ['alfie', 'woody', 'flynn', 'bink']
shelfFile['dogs'] = dogs
shelfFile.close()