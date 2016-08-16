def create_matrix(list1, list2):
    """Create and fill matrix for dynamic programming solution."""
    matrix = [[0 for j in range(len(list2)+1)] for i in range(len(list1)+1)]
    for i, x in enumerate(list1):
        for j, y in enumerate(list2):
            if x == y:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
    return matrix

def longest_common_subsequence(string1, string2):
    """Find the longest common subsequence between two string inputs.
    Subsequences are not required to occupy consecutive positions within inputs."""
    if not string1:
        return None
    if not string2:
        return None

    list1 = list(string1)
    list2 = list(string2)
    x = len(list1)
    y = len(list2)
    matrix = create_matrix(list1, list2)

    result = []
    while x != 0 and y != 0:
        if matrix[x][y] == matrix[x-1][y]:
            x -= 1
        elif matrix[x][y] == matrix[x][y-1]:
            y -= 1
        else:
            result.insert(0, list1[x-1])
            x -= 1
            y -= 1
    if len(result) > 0:
        return ''.join(result)
    else:
        return None
