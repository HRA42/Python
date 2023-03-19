if __name__ == "__main__":
    # Definiere Mengen
    U = {1, 3, 5, 7, 9, 11, 13}
    G = {2, 4, 6, 8, 10, 12}
    P = {1, 3, 5, 7, 11, 13, 17, 19, 23}
    # Operationen mit Mengen
    V = U.union(G)  # U | G
    S = U.intersection(P)  # U & P
    P_ohne_U = P.difference(U)  # P - U
    U_ohne_P = U.difference(P)  # U - P
    # Ausgabe
    print("U = ", U)
    print("G = ", G)
    print("P = ", P)
    print("Vereinigungsmenge \nU \u222A G = ", V)
    print("Schnittmenge\nU \u2229 P = ", S)
    print("Differenzmenge\nP \u2216 U = ", P_ohne_U)
    print("Differenzmenge\nU \u2216 P = ", U_ohne_P)
