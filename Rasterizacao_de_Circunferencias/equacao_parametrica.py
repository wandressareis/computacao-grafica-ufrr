import matplotlib.pyplot as plt 
import numpy as np

def equacaoParametrica(xc, yc, raio):
    x = xc + raio
    y = yc

    for t in range(1, 360 + 1, 1):
        plt.plot(round(x), round(y), marker='o', color='blue')

        x = xc + raio * np.cos(t*np.pi/180)
        y = yc + raio * np.sin(t*np.pi/180)
        
    plt.title('Equação Paramétrica', fontdict={'fontsize':12, 'fontweight':'bold'})
    plt.axis("equal") 
    plt.show()

def main():
    xc = int(input('Informe o valor de xc: '))
    yc = int(input('Informe o valor de yc: '))
    raio = int(input('Informe o valor do raio: '))

    equacaoParametrica(xc, yc, raio)

if __name__ == "__main__":
    main()