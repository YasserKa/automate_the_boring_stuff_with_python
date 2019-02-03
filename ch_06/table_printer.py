def printTable(tableData):

    colWidths = [0] * len(tableData)

    for i in range(len(tableData)):
        for string in (tableData[i]):
            if (colWidths[i] < len(string)):
                colWidths[i] = len(string)

    # print the elements that has the same index in each list
    for y in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][y].rjust(colWidths[x]), end = ' ')
        print('')

tableData = [
            ['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']
        ]

printTable(tableData)
