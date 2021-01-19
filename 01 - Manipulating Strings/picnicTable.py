def picnicTable(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, ' '))

picnicItems = {'sandwiches': 4, 'mars bar': 2, 'strawberries': 10, 'lemonade': 2}
picnicTable(picnicItems, 14, 2)
picnicTable(picnicItems, 30, 4)