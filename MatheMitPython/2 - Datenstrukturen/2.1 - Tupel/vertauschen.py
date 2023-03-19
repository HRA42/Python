if __name__ == "__main__":
    a, b = 17, 13
    T=(a,b)
    print("---vor dem Tausch---")
    print("a = %i   | b = %i" % (a, b))
    print("%i | %i" % (id(a), id(b)))
    print("T =", T, " id:", id(T))
    a,b=b,a
    print("---nach dem Tausch---")
    print("a = %i   | b = %i" % (a, b))
    print("%i | %i" % (id(a), id(b)))
    print("T =", T, " id:", id(T))
