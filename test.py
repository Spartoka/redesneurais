import numpy as np

entradas = np.array([1, 1])
pesos = np.array([[0.5, 1, 1],
                  [0.5, 1, 1]])

print(entradas.dot(pesos))