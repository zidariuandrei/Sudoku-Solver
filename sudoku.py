board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def solve(bo):
    find = findEmpty(bo)
    if not find :
        return True
    else:
        for i in range (1,10):
           if isValid(bo, i, find):
                row, column = find
                bo[row][column] = i

                if solve(bo):
                    return True

                bo[row][column] = 0

        return False               

def isValid(bo, number, pos):
    #check row
    for i in range(9):
        if bo[pos[0]][i] == number and pos[1] !=i :
            return False

    #check column
    for i in range(9):
        if bo[i][pos[1]] == number and pos[0] != i :
            return False

    #check division
    row = pos[1] // 3
    column = pos[0] // 3

    for i in range(column*3, column*3+3):
        for j in range(row*3, row*3+3):
            if bo[i][j] == number and pos[0]!=i and pos[1]!=j :
                return False
    return True



def printTable(b):
    for i in range(9):
        if i % 3 == 0 :
            print("_ _ _ _ _ _ _ _ _ _ _ _ _")
        print("|", end =" ")
        for j in range(9):
            if b[i][j] != 0:
                print(b[i][j], end =" ")
            else:
                 print(" ", end =" ")
            if j % 3 == 2 :
                print("|", end =" ")
        print("")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _")

def findEmpty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0 :
                return (i,j)


printTable(board)   
solve(board)
printTable(board)