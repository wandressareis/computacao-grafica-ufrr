import matplotlib.pyplot as plt

# MÉTODO ANALÍTICO
def metodoAnalitico(x1, y1, x2, y2):

  if x1 == x2: # reta vertical
    for Y in range(y1, y2 + 1): 
      plt.plot(x1, Y, marker='o', color='red')
      plt.title('Método Analítico', fontdict={ 'fontsize': 12, 'fontweight': 'bold' }) # Apenas intitulando o gráfico
  else:
    m = (y2 - y1)/(x2 - x1)
    b = y2 - m * x2
    for X in range(x1, x2 + 1):
      Y = m * X + b
      plt.plot(X, round(Y), marker='o', color='red')
      plt.title('Método Analítico', fontdict={ 'fontsize': 12, 'fontweight': 'bold' }) # Apenas intitulando o gráfico


# MÉTODO DDA (Analisador Diferencial Digital)
def metodoDDA(x1, y1, x2, y2):

  if abs(x2 - x1) > abs(y2 - y1): # |x2 - x1| > |y2 - y1|
    incremento = (y2 - y1) / (x2 - x1)
    Y = y1
    for X in range(x1, x2 + 1):
      # Reta horizontal
      plt.plot(X, round(Y), marker='o', color='blue')
      plt.title('Método DDA', fontdict={ 'fontsize': 12, 'fontweight': 'bold' })
      Y = Y + incremento
  else:
    # Demais casos
    incremento = (x2 - x1) / (y2 - y1)
    X = x1
    for Y in range(y1, y2 + 1):
      plt.plot(round(X), Y, marker='o', color='blue')
      plt.title('Método DDA', fontdict={ 'fontsize': 12, 'fontweight': 'bold' })
      X = X + incremento


# MÉTODO BRESENHAM
def metodoBresenham(x1, y1, x2, y2):
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
                plt.plot(Y, -X, marker='o', color='green')
            else:
                # 3 e 9
                plt.plot(Y, X, marker='o', color='green')

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
                plt.plot(X, -Y, marker='o', color='green')
            else:
                # 9 e 3
                plt.plot(X, Y, marker='o', color='green')

            if(parametro < 0):
                parametro = parametro + 2*delta_y
            else:
                Y = Y + 1
                parametro = parametro + 2*(delta_y - delta_x)