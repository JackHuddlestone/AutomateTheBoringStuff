tableData = [['apples','oranges','cherries','banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(table)
    
    #Find the longest string in each list within the table.
    for i in range(len(table)):           # List in TableData
        maxWidth = 0
        for j in range(len(table[i])):    # Item in list
            width = len(table[i][j])
            if width > maxWidth:
                maxWidth = width
                colWidths[i] = maxWidth
    
    #Rotate the printing
    for x in range(len(table[0])) :
        for y in range(len(table)) :
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print()

printTable(tableData)

    