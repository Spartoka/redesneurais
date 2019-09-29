import numpy as np

entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saidas = np.array([0, 1, 1, 1])
pesos = np.array([0.0, 0.0])
taxaAp = 0.1


def processo(registro):
    return stepFunction(registro.dot(pesos))


def stepFunction(resultado):
    if resultado >= 1:
        return 1
    return 0


def treinar():
    erro_total = 1
    contagem = 0
    ajustes = 0
    while erro_total != 0:
        erro_total = 0
        print('----CICLO {}----'.format(contagem))
        contagem += 1
        for i in range(len(entradas)):
            entrada = np.array(entradas[i])
            resultado = processo(entrada)
            erro = abs(saidas[i] - resultado)
            erro_total += erro
            print('TESTE ENTRADA {}\n'.format(i+1))
            print('Peso atual: ', pesos)
            print('({},  {}) -> {}'.format(entrada[0], entrada[1], resultado))
            print('')
            if erro > 0:
                for j in range(len(pesos)):
                    pesos[j] = pesos[j] + (entradas[i][j] * taxaAp * erro)
                print('Pesos atualizados: ', pesos)
                ajustes += 1
        print('Total  de erros: ', erro_total)
        print('')
        print('----END CICLO----')
        print('')
    print('TOTAL DE AJUSTES:', ajustes)
    return contagem


print('Ciclos necessarios:', treinar())
