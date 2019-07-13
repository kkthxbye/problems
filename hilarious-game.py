from random import randint
from sys import stdin

print("Welcome to answer the question, see how many points you can get!\n"
      " to quit just press enter before you answer a question")
points = 0
check = lambda v: ("you get +1 point!", 1) if sum(v) == int(stdin.readline()) else ("", 0)
for _ in range(0, 3):
    values = [randint(1, 99) for _ in range(0, 2)]
    print(f"question {' + '.join(str(x) for x in values)}  = ? ")
    r = check(values)
    print()
    if sum(values) == int(stdin.readline()):
        print("you get +1 point!")
        points += 1
    print(f"you have {points} point")
print(f"congratulations you earned {points} points")
