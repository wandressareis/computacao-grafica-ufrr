import numpy as np
import matplotlib.pyplot as plt

def de_casteljau(P0, P1, P2, P3, t):
    
    # Algoritmo de De Casteljau para subdividir a curva de Bézier recursivamente
  
    if t > 0.05:
        e = t / 2
        P0N1, P1N1, P2N1, P3N1, P0N2, P1N2, P2N2, P3N2 = ponto_medio_curva(P0, P1, P2, P3)
        de_casteljau(P0N1, P1N1, P2N1, P3N1, e)
        de_casteljau(P0N2, P1N2, P2N2, P3N2, e)
    else:
        plt.plot(*zip(*[P0, P1, P2, P3]), 'b-')

def ponto_medio_curva(P0, P1, P2, P3):
    # Calcula os pontos médios para subdivisão da curva
    M01 = (np.array(P0) + np.array(P1)) / 2
    M12 = (np.array(P1) + np.array(P2)) / 2
    M23 = (np.array(P2) + np.array(P3)) / 2

    M012 = (M01 + M12) / 2
    M123 = (M12 + M23) / 2

    M0123 = (M012 + M123) / 2

    plt.plot(M0123[0], M0123[1], 'b-')  # Desenhar pontos da curva
    
    return P0, M01, M012, M0123, M0123, M123, M23, P3

def plot_bezier():
    # Função para configurar a curva Bézier e iniciar a subdivisão
    P0, P1, P2, P3 = (0, 0), (1, 2), (3, 3), (4, 0)
    
    plt.figure(figsize=(6, 6))
    plt.plot(*zip(*[P0, P1, P2, P3]), 'go--', label='Pontos de Controle')  # Desenha os pontos de controle
    de_casteljau(P0, P1, P2, P3, 1)
    
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_bezier()
