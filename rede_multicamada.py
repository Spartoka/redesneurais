import numpy as np


def sigmoid(soma):  # Função calcular resultado
    return 1 / (1 + np.exp(-soma))


entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],  # Pesos das entradas
                   [0.358, -0.577, -0.469]])

pesos1 = np.array([[-0.017], [-0.895], [0.148]])  # Pesos das camadas ocultas

epocas = 100  # Quantas vezes ele vai executar o treino

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
