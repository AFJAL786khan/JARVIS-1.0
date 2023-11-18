from sympy import symbols

x, y = symbols(('x y'))
expr = x + 2*y
expr = expr - x
print(expr)