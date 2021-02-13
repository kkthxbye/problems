def numberOfSteps(num: int) -> int:
    steps = 0
    while num != 0:
        num = num / 2 if num % 2 == 0 else num - 1
        steps += 1
    return steps


print(numberOfSteps(14))

print(numberOfSteps(8))
