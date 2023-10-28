A = int(input())
B = int(input())
squares = [i**2 for i in range(A, B+1)]

for square in squares:
    print(square)