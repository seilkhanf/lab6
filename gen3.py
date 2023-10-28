n = int(input())
nums = [i for i in range(n + 1) if i % 3 == 0 and i % 4 == 0]
for num in nums:
    print(num)