import numpy as np
import matplotlib.pyplot as plt

def circulo_bresenham(matriz, yc, xc, raio):
    x = 0
    y = raio
    p = 1 - raio # parâmetro

    while x <= y:  # no slide: x != y
        matriz[ x + xc,  y + yc] = 1
        matriz[ y + xc,  x + yc] = 1
        matriz[-y + xc,  x + yc] = 1
        matriz[-x + xc,  y + yc] = 1
        matriz[-x + xc, -y + yc] = 1
        matriz[-y + xc, -x + yc] = 1
        matriz[ y + xc, -x + yc] = 1
        matriz[ x + xc, -y + yc] = 1
        if p >= 0:
            y = y - 1
            p = p + 2*x - 2*y + 5
            x = x + 1
        else:
            p = p + 2*x + 3
            x = x + 1   

def metodoBresenham(matriz, x1, y1, x2, y2):
    if x1 > x2: 
      x1, x2 = x2, x1
      y1, y2 = y2, y1

    inverte = False

    if y1 >= y2:
        y1 = -y1
        y2 = -y2
        inverte = True
    
    delta_y = y2 - y1
    delta_x = x2 - x1

    if abs(delta_y) > abs(delta_x):
        x1, y1 = y1, x1
        x2, y2 = y2, x2

        delta_y = y2 - y1
        delta_x = x2 - x1

        Y = y1

        parametro = 2*delta_y - delta_x
        for X in range(x1, x2 + 1):
            if inverte:
                # Vertical
                # plt.plot(Y, -X, marker='o', color='green')
                matriz[-X, Y] = 1
            else:
                # 3 e 9
                # plt.plot(Y, X, marker='o', color='green')
                matriz[X, Y] = 1

            if(parametro < 0):
                parametro = parametro + 2*delta_y
            else:
                Y = Y + 1
                parametro = parametro + 2*(delta_y - delta_x)
    else:
        Y = y1

        parametro = 2*delta_y - delta_x
        for X in range(x1, x2 + 1):
            if(inverte):
                # Horizontal
                # plt.plot(X, -Y, marker='o', color='green')
                matriz[-Y, X] = 1
            else:
                # 9 e 3
                # plt.plot(X, Y, marker='o', color='green')
                matriz[Y, X] = 1

            if(parametro < 0):
                parametro = parametro + 2*delta_y
            else:
                Y = Y + 1
                parametro = parametro + 2*(delta_y - delta_x)

def desenha_retangulo(matriz, x_topo_esquerdo, y_topo_esquerdo, largura, altura):
    metodoBresenham(matriz, x_topo_esquerdo, y_topo_esquerdo, x_topo_esquerdo + largura, y_topo_esquerdo)
    metodoBresenham(matriz, x_topo_esquerdo, y_topo_esquerdo + altura, x_topo_esquerdo + largura, y_topo_esquerdo + altura)
    metodoBresenham(matriz, x_topo_esquerdo, y_topo_esquerdo, x_topo_esquerdo, y_topo_esquerdo + altura)
    metodoBresenham(matriz, x_topo_esquerdo + largura, y_topo_esquerdo, x_topo_esquerdo + largura, y_topo_esquerdo + altura)

def desenha_hexagono(matriz):
    metodoBresenham(matriz, 50, 24, 86, 48)
    metodoBresenham(matriz, 50, 24, 20, 42)
    metodoBresenham(matriz, 20, 42, 44, 54)
    metodoBresenham(matriz, 86, 48, 80, 60)
    metodoBresenham(matriz, 44, 54, 32, 66)
    metodoBresenham(matriz, 32, 66, 80, 60)

def desenha_octagono(matriz):
    metodoBresenham(matriz, 21, 24, 41, 24)
    metodoBresenham(matriz, 41, 24, 49, 30)
    metodoBresenham(matriz, 49, 30, 57, 24)
    metodoBresenham(matriz, 57, 24, 77, 24)
    metodoBresenham(matriz, 77, 24, 77, 42)
    metodoBresenham(matriz, 77, 42, 49, 60)
    metodoBresenham(matriz, 49, 60, 21, 42)
    metodoBresenham(matriz, 21, 42, 21, 24)

def flood_fill(matriz, x, y, cor, nova_cor):
    if x < 0 or x >= matriz.shape[0] or y < 0 or y >= matriz.shape[1]:
        return
    # se o ponto[x, y] for igual a cor, receberá nova_cor
    if matriz[y, x] == cor: 
        matriz[y, x] = nova_cor 

        flood_fill(matriz, x + 1, y, cor, nova_cor)
        flood_fill(matriz, x - 1, y, cor, nova_cor)
        flood_fill(matriz, x, y + 1, cor, nova_cor)
        flood_fill(matriz, x, y - 1, cor, nova_cor)