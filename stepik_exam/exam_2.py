# Input is some matrix and is interrupted by special line "==="
# Print matrix with the same dimensions as input
# i,j -th element is 1 if i,j -th element of input have from 3 to 6 neighbours with 1 value

# Read matrix
matrix = []
while True:
    new_str = input()
    if new_str == "===":
        break
    else:
        matrix.append(list(map(int, new_str.split())))

# Calculate dimensions
nrows = len(matrix)
ncols = len(matrix[0])

# For all elements
for i in range(nrows):
    for j in range(ncols):
        ones = - matrix[i][j]
        for m in range(-1, 2):
            for n in range(-1, 2):
                row = (i + m) % nrows
                col = (j + n) % ncols
                if matrix[row][col] == 1:
                    ones += 1
        if 3 <= ones <= 6:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
