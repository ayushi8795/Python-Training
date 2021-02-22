try:
    eval("x === x")
except SyntaxError:
    print("only == allowed")