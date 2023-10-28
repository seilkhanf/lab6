b = int(input("number: "))

even_num = [a for a in range(0, b + 1, 2)]
r = ", ".join(map(str, even_num))

print("even numb between zero and ", b, "commaform:")
print(r)