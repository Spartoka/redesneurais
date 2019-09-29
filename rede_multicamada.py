import numpy as np

entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])

saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-0.424, -0.740, -0.961],  # Pesos das entradas x
                   [0.358, -0.577, -0.469]])  # Pesos das entradas y

pesos1 = np.array([[-0.017], [-0.895], [0.148]])  # Pesos das camadas ocultas

epocas = 100  # Quantas vezes ele vai executar o treino


def sigmoid(soma):  # Função calcular resultado
    return 1 / (1 + np.exp(-soma))


def camadaOculta():
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    return sigmoid(somaSinapse0)


def camadaSaida():
    somaSinapse1 = np.dot(camadaOculta(), pesos1)
    return sigmoid(somaSinapse1)


def treinar():
    erroCamadaSaida = saidas - camadaSaida()
    mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))
    return mediaAbsoluta


print(treinar())
