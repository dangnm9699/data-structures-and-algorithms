

def calculate_expression(s:str)->int:
    values = []
    operators = []

    i = 0

    while i < len(s):
        # if empty char
        if s[i] == ' ':
            i += 1
            continue
        # if open brace
        elif s[i] == '(':
            operators.append(s[i])
        # if digit
        elif s[i].isdigit():
            # check if next char is a digit
            value = int(s[i])
            while i+1 < len(s) and s[i+1].isdigit():
                value = 10*value + int(s[i+1])
                i+=1
            values.append(value)
        # if close brace
        elif s[i] == ')':
            # calculate value in braces
            while len(operators) != 0 and operators[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = operators.pop()

                values.append(_result(val1, val2, op))
            # pop open brace
            operators.pop()
        # if operator
        else:
            # if the priority of the last operator greater than this operator
            while len(operators) != 0 and _prioiry(operators[-1]) > _prioiry(s[i]):
                # calculate
                val2 = values.pop()
                val1 = values.pop()
                op = operators.pop()

                values.append(_result(val1, val2, op))
            operators.append(s[i])
        i += 1
    while len(operators) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = operators.pop()

        values.append(_result(val1, val2, op))
    return values[0]

def _prioiry(op:str)->int:
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def _result(val1:int, val2:int, op:str)->int:
    if op == '+':
        return val1 + val2
    if op == '-':
        return val1 - val2
    if op == '*':
        return val1 * val2
    if op == '/':
        return val1 // val2
