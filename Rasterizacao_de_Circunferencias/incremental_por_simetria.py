import matplotlib.pyplot as plt 
import numpy as np

def alg_incremental_com_simetria(xc, yc, raio):
    R = raio
    x = R
    y = 0
    teta = 1/R
    C = np.cos(teta)
    S = np.sin(teta)

    while y <= x:
        plt.plot(round(x + xc), round(y + yc), marker='o', color='blue')
        plt.plot(round(y + xc), round(x + yc), marker='o', color='red')
        plt.plot(round(-y + xc), round(x + yc), marker='o', color='yellow')
        plt.plot(round(-x + xc), round(y + yc), marker='o', color='pink')
        plt.plot(round(-x + xc), round(-y + yc), marker='o', color='grey')
        plt.plot(round(-y + xc), round(-x + yc), marker='o', color='black')
        plt.plot(round(y + xc), round(-x + yc), marker='o', color='orange')
        plt.plot(round(x + xc), round(-y + yc), marker='o', color='green')

        Xtemp = x
        x = x*C - y*S
        y = y*C + Xtemp*S

    plt.plot(round(x + xc), round(y + yc), marker='o', color='blue')
    plt.plot(round(y + xc), round(x + yc), marker='o', color='red')
    plt.plot(round(-y + xc), round(x + yc), marker='o', color='yellow')
    plt.plot(round(-x + xc), round(y + yc), marker='o', color='pink')
    plt.plot(round(-x + xc), round(-y + yc), marker='o', color='grey')
    plt.plot(round(-y + xc), round(-x + yc), marker='o', color='black')
    plt.plot(round(y + xc), round(-x + yc), marker='o', color='orange')
    plt.plot(round(x + xc), round(-y + yc), marker='o', color='green')
        
    plt.title('Algoritmo Incremental com Simetria', fontdict={'fontsize':12, 'fontweight':'bold'})
    plt.axis("equal")
    plt.show()
    
def main():
    xc = int(input('Informe o valor de xc: '))
    yc = int(input('Informe o valor de yc: '))
    raio = int(input('Informe o valor do raio: '))

    alg_incremental_com_simetria(xc, yc, raio)

if __name__ == "__main__":
    main()