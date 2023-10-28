nums = [int(input()) for _ in range(3)]
output = 3 if nums[0] == nums[1] == nums[2] else 2 if nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2] else 0
print(output)