from pathlib import Path

helloFile = open('04 - Reading And Writing Files/sonnet.txt')
lines = helloFile.readlines()
for line in lines:
    print(line)

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, World!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)