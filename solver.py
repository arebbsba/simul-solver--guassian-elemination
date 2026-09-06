def solve_system(matrix):
    """
    matrix: list of lists, each inner list is a row of coefficients
    followed by the constant, e.g. for:
        2x + 3y - z = 5
        4x + y + 2z = 6
        -2x + 5y - z = 3
    matrix = [
        [2, 3, -1, 5],
        [4, 1, 2, 6],
        [-2, 5, -1, 3]
    ]
    """
    n = len(matrix)

    # Forward elimination
    for i in range(n):
        # Partial pivoting: swap to avoid dividing by zero/small numbers
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("No unique solution exists")

        for j in range(i + 1, n):
            factor = matrix[j][i] / pivot
            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Back substitution
    solutions = [0] * n
    for i in range(n - 1, -1, -1):
        solutions[i] = matrix[i][n]
        for j in range(i + 1, n):
            solutions[i] -= matrix[i][j] * solutions[j]
        solutions[i] /= matrix[i][i]

    return solutions


# Example usage
system = [
    [2, 3, -1, 5],
    [4, 1, 2, 6],
    [-2, 5, -1, 3]
]
print(solve_system(system))
