from math import factorial as fac
import matplotlib.pyplot as plt

def binomio_newton(n, i): # Definindo a 
    return fac(n) / (fac(i) * fac(n - i))

def polinomio_bernstein(n, i, t):
    return binomio_newton(n, i) * (t**i) * ((1 - t)**(n - i))

def curva_bezier(pontos):
    n = len(pontos) - 1
    curva = []
    
    for c in range(0, 100 + 1):
        t = c / 100  # definindo t no range (0, 1)
        x_soma = sum(polinomio_bernstein(n, i, t) * pontos[i][0] for i in range(n + 1)) # 
        y_soma = sum(polinomio_bernstein(n, i, t) * pontos[i][1] for i in range(n + 1))
        curva.append((x_soma, y_soma))

    return curva

def main():
    pontos = [(0, 0), (1, 2), (3, 3), (4, 0)]
    curva = curva_bezier(pontos)

    curva_x, curva_y = zip(*curva)
    plt.plot(curva_x, curva_y, 'b-', label='Curva de Bézier - Eq Paramétrica')
    
    pontos_x, pontos_y = zip(*pontos)
    plt.plot(pontos_x, pontos_y, 'ro--', label='Pontos de Controle')
    
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
