import numpy as np

if __name__ == "__main__":
    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    B = np.array([[9, 8, 7],
                  [6, 5, 4],
                  [3, 2, 1]])
    # Matrixmultiplikation
    # Infinixoperator
    C1 = A@B
    C2 = B@A
    # Methode
    # C = np.matmul(A, B)
    # Ausgabe
    print("Matrix A\n", A)
    print("Zugriff auf A[1, 1] = ", A[1,1])
    print("Transponierte von A\n", A.T)
    print("Matrix B\n", B)
    print("Transponierte von B\n", B.T)
    print("Multiplikation A@B\n", C1)
    print("Multiplikation B@A\n", C2)
    print("Multiplikation (A@B).T\n", (A@B).T)
    print("Multiplikation B.T@A.T\n", B.T@A.T)
    