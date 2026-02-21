A = [[0] *3  for i in range (3)]
def init_table(A):
    k = 1
    for i in range(3):
        for j in range(3):
            A [i][j] = k
            k += 1
def table(A):
    for i in range(3):
        for j in range(3):
            print(A[i][j], end='   ')
        print()  
init_table(A)
table(A)
def put(x, s):
    row = x//3
    c = x%3
    if A[row][c] == "X" or A[row][c] == "O":
        print(":(")
        exit(0)
    A[row][c] = s
def check_win(s):
    for i in range(3): 
        if A[i][0]==s and A[i][1] ==s and A[i][2]==s:
            return True
        if A[0][i]==s and A[1][i] ==s and A[2][i]==s:
            return True
    if A[0][0]==s and A[1][1] ==s and A[2][2]==s:
         return True
    if A[0][2]==s and A[1][1] ==s and A[2][0]==s:
        return True
    return False
for mov in range(9):
    if mov % 2 == 0:
        x = int(input('Player 1:'))
        put(x-1, "X")
        if check_win("X"):
            print('Player 1 won!')
            break
    else:
        x = int(input('Player 2:'))
        put(x-1, "O")
        if check_win('O'):
            print('player2 won!')
            break 
    table(A)