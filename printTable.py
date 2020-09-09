#! python3
# printTable 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0]*len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    for i in range(len(tableData[0])):
        for j in range(len(colWidths) - 1):
            print(tableData[j][i].rjust(colWidths[j]), end = ' ')
        print(tableData[-1][i].rjust(colWidths[-1]))

printTable(tableData)