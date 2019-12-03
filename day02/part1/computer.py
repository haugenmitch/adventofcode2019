import sys

with open(sys.argv[1]) as f:
    nums = [int(x) for x in f.read().split(',')]

pc = 0

while pc < len(nums):
    if nums[pc] == 1:
        nums[nums[pc+3]] = nums[nums[pc+1]] + nums[nums[pc+2]]
    elif nums[pc] == 2:
        nums[nums[pc+3]] = nums[nums[pc+1]] * nums[nums[pc+2]]
    else:
        break

    pc = pc + 4

print(nums[0])
