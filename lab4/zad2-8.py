def params(*args):
    # for i, param in enumerate(args, start=1):
    #     print(f"param {i}: {param}")
    maksymalna = max(args)
    return f"Wartość maksymalna: {maksymalna}"
wynik = params(1,2,3,55,9)
print(wynik)