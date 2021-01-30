import shelve
shelfFile = shelve.open('data')
print(type(shelfFile))
print(shelfFile['dogs'])
print(list(shelfFile.items()))
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()