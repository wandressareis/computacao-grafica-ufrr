import matplotlib.pyplot as plt 

def bresenham(xc, yc, raio):
    x = 0
    y = raio
    p = 1 - raio # parâmetro

    while x <= y:  # no slide: x != y
        plt.plot(x + xc, y + yc, marker='o', color='blue')
        plt.plot(y + xc, x + yc, marker='o', color='red')
        plt.plot(-y + xc, x + yc, marker='o', color='yellow')
        plt.plot(-x + xc, y + yc, marker='o', color='pink')
        plt.plot(-x + xc, -y + yc, marker='o', color='grey')
        plt.plot(-y + xc, -x + yc, marker='o', color='black')
        plt.plot(y + xc, -x + yc, marker='o', color='orange')
        plt.plot(x + xc, -y + yc, marker='o', color='green')

        if p >= 0:
            y = y - 1
            p = p + 2*x - 2*y + 5
            x = x + 1
        else:
            p = p + 2*x + 3
            x = x + 1   


    plt.axis('equal')
    plt.show()
    
def main():
    xc = int(input('Informe o valor de xc: '))
    yc = int(input('Informe o valor de yc: '))
    raio = int(input('Informe o valor do raio: '))

    bresenham(xc, yc, raio)

if __name__ == "__main__":
    main()