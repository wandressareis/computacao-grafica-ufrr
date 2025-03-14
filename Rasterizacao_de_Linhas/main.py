from algoritmos import metodoAnalitico, metodoDDA, metodoBresenham
import matplotlib.pyplot as plt
import numpy as np

print('------------- RASTERIZAÇÃO LINEAR ---------------')

print('[1] Analítico')
print('[2] DDA')
print('[3] Bresenham')

print('Qual algoritmo deseja utilizar?')
escolha = int(input())

# Definindo os pontos
x1 = int(input('Infome o valor de x1: '))
y1 = int(input('Informe o valor de y1: '))
x2 = int(input('Informe o valor de x2: '))
y2 = int(input('Informe o valor de y2: '))

if escolha == 1:
  metodoAnalitico(x1, y1, x2, y2)
elif escolha == 2:
  metodoDDA(x1, y1, x2, y2)
elif escolha == 3:
  metodoBresenham(x1, y1, x2, y2)

# Configurando os ticks para valores inteiros
plt.axis('equal')
plt.xticks(np.arange(min(x1, x2), max(x1, x2) + 1, 1))
plt.yticks(np.arange(min(y1, y2), max(y1, y2) + 1, 1))
plt.xticks(np.arange(min(x1, x2), max(x1, x2), 1), minor=True)
plt.yticks(np.arange(min(y1, y2), max(y1, y2), 1), minor=True)

plt.grid(True)
#Plotando o gráfico
plt.show()