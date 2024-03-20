dimension = int(input("Ingrese un numero "))
spiral = []
for _ in range(dimension):
    row = []
    for _ in range(dimension):
        row.append(0)
    spiral.append(row)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  #Derecha, abajo, izquierda, derecha
direction = 0
num = 1
row = 0
col = 0
while num <= dimension ** 2:
    spiral[row][col] = num
    num += 1
    next_row = row + directions[direction][0]
    next_col = col + directions[direction][1]

    if (((0 <= next_row < dimension) and (0 <= next_col < dimension)) and (spiral[next_row][next_col] == 0)):
        row = next_row
        col = next_col
    else:
        direction = (direction + 1) % 4
        row += directions[direction][0]
        col += directions[direction][1]
max_width = len(str(dimension ** 2))
for row in spiral:
    for num in row:
        print(f"{num:{max_width}}", end=" ")
    print()