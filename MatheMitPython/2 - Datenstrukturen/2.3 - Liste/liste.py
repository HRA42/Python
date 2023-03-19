if __name__ == "__main__":
    U = [1, 3, 5, 7, 11, 13, 15]
    G = [2, 4, 6, 8, 10, 12, 14]
    R = list(reversed(G))
    summe = sum(U)
    UG = U + G
    Z = list(zip(U, G))
    print("U = ", U)
    print("G = ", G)
    print("G[2:5]", G[2:5])
    print("Reihenfolge von G umkehren\n", R)
    print("Anzahl der Elemente von U: n= ", len(U))
    print("Summe von U = ", summe)
    print("Liste G an Liste U anfügen\n", UG)
    print("Liste sortieren\n", sorted(UG))
    print("Liste verketten\n", Z)
    print(type(Z))
