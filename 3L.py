k = int(input())
n = int(input())

result = [n // k, n % k]
print(*result, sep="\n")