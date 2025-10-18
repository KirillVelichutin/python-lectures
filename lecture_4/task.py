numRows = int(input("Сколько строк вы хотите вывести?: "))

triangle = [[1]]

for i in range(numRows - 1):
    constructor = [0] + triangle[-1] + [0]
    newRow = []
    for j in range(len(triangle[-1]) + 1):
        newRow.append(constructor[j] + constructor[j + 1])
    
    triangle.append(newRow)

for row in triangle:
    print(row)