import itertools

data = open('day_7/data.txt', 'r').read().splitlines()
data = [x.split(": ") for x in data]
answer = [int(x[0]) for x in data]
number = [[int(y) for y in x[1].split()] for x in data]

solution = 0
for ans, nums in zip(answer, number):
    # repeat is the number of empty spaces of each line of nums
    operation_combinations = list(itertools.product(['+', '*'], repeat=len(nums)-1))
    for i in range(len(operation_combinations)):
        result = nums[0]
        for j in range(len(operation_combinations[i])):
            if operation_combinations[i][j] == '+':
                result += nums[j+1]
            elif operation_combinations[i][j] == '*':
                result *= nums[j+1]
        if result == ans:
            solution += result
            break

print('Part 1:', solution)


solution2 = 0
for ans, nums in zip(answer, number):
    # repeat is the number of empty spaces of each line of nums
    operation_combinations = list(itertools.product(['+', '*', '||'], repeat=len(nums)-1))
    for i in range(len(operation_combinations)):
        result = nums[0]
        for j in range(len(operation_combinations[i])):
            if operation_combinations[i][j] == '+':
                result += nums[j+1]
            elif operation_combinations[i][j] == '*':
                result *= nums[j+1]
            elif operation_combinations[i][j] == '||': #just add this thingy lol. python is so easy
                result = int(str(result) + str(nums[j+1]))
        if result == ans:
            solution2 += result
            break

print('Part 2:', solution2)
