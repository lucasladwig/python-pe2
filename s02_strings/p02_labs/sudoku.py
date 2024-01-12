# Your task is to write a program which:
# * reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
# * outputs Yes if the Sudoku is valid, and No otherwise.


def check_sudoku() -> str:
    """Checks if the given board is a valid sudoku solution."""

    board = [[int(char) for char in input()] for _ in range(9)]
    
    # Definir estado inicial como verdadeiro
    sudoku = True

    # Percorrer linhas e testar
    for l in range(9):
        group = set(board[l])
        if len(group) != 9:
            sudoku = False
            break

    # Percorrer colunas e testar
    if sudoku:
        for c in range(9):
            group = set(board[l][c] for l in range(9))
            if len(group) != 9:
                sudoku = False
                break

    # Percorrer quadrantes 3x3 e testar
    if sudoku:
        for c in (0, 3, 6):
            for l in (0, 3, 6):
                group = set(board[l][c:c+3] + board[l+1][c:c+3] + board[l+2][c:c+3])
                if len(group) != 9:
                    sudoku = False
                    break
    
    # Retornar resultado no formato
    if sudoku:
        return("Yes")
    else:
        return("No")

# Run Program
print(check_sudoku())