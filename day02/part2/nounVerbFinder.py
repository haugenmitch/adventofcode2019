import copy, sys

with open(sys.argv[1]) as f:
    originalNums = [int(x) for x in f.read().split(',')]

for noun in range(100):
    for verb in range(100):
        nums = copy.deepcopy(originalNums)
        nums[1] = noun
        nums[2] = verb

        pc = 0

        while pc < len(nums):
            if nums[pc] == 1:
                nums[nums[pc+3]] = nums[nums[pc+1]] + nums[nums[pc+2]]
            elif nums[pc] == 2:
                nums[nums[pc+3]] = nums[nums[pc+1]] * nums[nums[pc+2]]
            else:
                break

            pc = pc + 4

        if nums[0] == 19690720:
            print('Noun: ' + str(noun) + ' Verb: ' + str(verb))
            break

    else:
        continue
    break
