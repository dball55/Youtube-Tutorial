#Rows and Columns Generator

rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))
symbol = (input("Symbol to use: "))

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()



