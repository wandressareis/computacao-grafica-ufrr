from flood_fill import circulo_bresenham, flood_fill, metodoBresenham, desenha_retangulo, desenha_hexagono, desenha_octagono
import matplotlib.pyplot as plt
import sys
import numpy as np

sys.setrecursionlimit(50000)
size = 100

def main():
    print('------------------------- Algoritmo Flood Fill --------------------------')
    
    print('[1] Pinte um círculo')
    print('[2] Pinte um retângulo')
    print('[3] Pinte um hexágono côncavo irregular')
    print('[4] Pinte um octágono côncavo irregular')

    print('Informe o número da forma que deseja preencher: ')
    escolha = int(input())

    if escolha == 1:
        # xc = int(input('Informe o valor de xc: '))
        # yc = int(input('Informe o valor de yc: '))
        # raio = int(input('Informe o valor do raio: '))

        # Criar matriz
        matriz_circulo = np.zeros((size, size));
        circulo_bresenham(matriz_circulo, 50, 50, 30)
        flood_fill(matriz_circulo, 45, 42, 0, 2)
        plt.matshow(matriz_circulo)
        plt.show()

        # matriz_metodoBresenham = np.zeros((size, size))
        # metodoBresenham(matriz_metodoBresenham, x1, y1, x2, y2)
        # plt.matshow(matriz_metodoBresenham)
        # plt.show()
    elif escolha == 2:
        matriz_retangulo = np.zeros((size, size))
        desenha_retangulo(matriz_retangulo, 18, 30, 60, 30)
        flood_fill(matriz_retangulo, 44, 48, 0, 2)
        plt.matshow(matriz_retangulo)
        plt.show()
    elif escolha == 3:
        matriz_hexagono = np.zeros((size, size))
        desenha_hexagono(matriz_hexagono)
        flood_fill(matriz_hexagono, 42, 39, 0, 2)
        plt.matshow(matriz_hexagono)
        plt.show()
    elif escolha == 4:
        matriz_octagono = np.zeros((size, size))
        desenha_octagono(matriz_octagono)
        flood_fill(matriz_octagono, 49, 39, 0, 2)
        plt.matshow(matriz_octagono)
        plt.show()
        
    
if __name__ == "__main__":
    main()