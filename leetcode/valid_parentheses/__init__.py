#

def parentheses_are_valid(s: str) -> bool:
    stack = []
    parentheses = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for c in s:
        if c in parentheses.values():
            stack.append(c)
        elif stack and stack[-1] == parentheses[c]:
            stack.pop()
        else:
            return False
    return not stack


print(parentheses_are_valid('(({}))[{}]()'))
print(parentheses_are_valid('()'))
print(parentheses_are_valid('())'))
