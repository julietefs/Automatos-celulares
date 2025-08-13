import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

VAZIO = 0
ARVORE = 1
FOGO = 2

def inicializar_floresta(tamanho, densidade=0.6):
    return np.random.choice([VAZIO, ARVORE], size=(tamanho, tamanho), p=[1 - densidade, densidade])

def iniciar_fogo(floresta, linha=None, coluna=None):
    if linha is None:
        linha = floresta.shape[0] // 2
    if coluna is None:
        coluna = floresta.shape[1] // 2
    floresta[linha, coluna] = FOGO

def propagar_fogo(floresta):
    nova_floresta = floresta.copy()
    linhas, colunas = floresta.shape
    for i in range(linhas):
        for j in range(colunas):
            if floresta[i, j] == FOGO:
                nova_floresta[i, j] = VAZIO
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < linhas and 0 <= nj < colunas:
                        if floresta[ni, nj] == ARVORE:
                            nova_floresta[ni, nj] = FOGO
    return nova_floresta

def atualizar(frame, img, floresta):
    nova_floresta = propagar_fogo(floresta[0])
    floresta[0] = nova_floresta
    img.set_data(nova_floresta)
    return img,

def simular(tamanho=50, densidade=0.6, interval=300):
    floresta = [inicializar_floresta(tamanho, densidade)]
    iniciar_fogo(floresta[0])

    fig, ax = plt.subplots()
    img = ax.imshow(floresta[0], cmap=plt.cm.get_cmap('hot', 3), vmin=0, vmax=2)
    ani = animation.FuncAnimation(fig, atualizar, fargs=(img, floresta),
                                  frames=50, interval=interval, repeat=False)
    plt.title("Propagação de Incêndio em Floresta")
    plt.colorbar(img, ticks=[0, 1, 2], label="Estado")
    plt.show()


simular()
