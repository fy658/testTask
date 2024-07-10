def reverse_list(l:list):
    """
    Reverse a list without using any built in functions

    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    left = 0
    right = len(l) - 1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1

    return l


def solve_sudoku(matrix):
    """
    Write a programme to solve 9x9 Sudoku board.

    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle, Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.
    """

    def is_valid(num, pos):
        # Check row
        for col in range(9):
            if matrix[pos[0]][col] == num and pos[1] != col:
                return False

        # Check column
        for row in range(9):
            if matrix[row][pos[1]] == num and pos[0] != row:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if matrix[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty():
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == 0:
                    return (i, j)
        return None

    def solve():
        empty = find_empty()
        if not empty:
            return True

        row, col = empty
        for num in range(1, 10):
            if is_valid(num, (row, col)):
                matrix[row][col] = num
                if solve():
                    return True
                matrix[row][col] = 0

        return False

    solve()
    return matrix
