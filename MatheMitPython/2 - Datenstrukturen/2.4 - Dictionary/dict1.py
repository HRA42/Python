if __name__ == "__main__":
    f_x = ['sin(x)', 'cos(x)', 'ln(x)', 'sinh(x)', 'cosh(x)']
    f_1 = ['cos(x)', '-sin(x)', '1/x', 'cosh(x)', 'sinh(x)']
    dicA = dict(zip(f_x, f_1))
    print(dicA.keys())
    print(dicA.values())
    print(dicA)
    print("Ableitungen")
    print("1. Ableitung von sin(x):", dicA['sin(x)'])
    print("1. Ableitung von cos(x):", dicA['cos(x)'])
    print("1. Ableitung von ln(x):", dicA['ln(x)'])
    print("1. Ableitung von sinh(x):", dicA['sinh(x)'])
    print("1. Ableitung von cosh(x):", dicA['cosh(x)'])