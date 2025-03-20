import numpy as np
import matplotlib.pyplot as plt

def sutherland_hodgman(poligono, x_min, y_min, x_max, y_max): # lista de vértices de poligonos e coordenadas da janela de recorte
    saida = poligono 

    def recortar_borda(dentro, intersecao): 
        nonlocal saida 
        entrada = saida  
        saida = []
        
        n = len(entrada) 
        for i in range(0, n):  
            j = (i + 1) % n  # obtém o índice do prox vértice
            atual = entrada[i]
            proximo = entrada[j] 

            atual_dentro = dentro(atual) # verifica a posição atual 
            proximo_dentro = dentro(proximo)

            if atual_dentro and proximo_dentro:
                saida.append(proximo)
            elif atual_dentro and not proximo_dentro:
                saida.append(intersecao(atual, proximo))
            elif not atual_dentro and proximo_dentro:
                saida.append(intersecao(atual, proximo))
                saida.append(proximo)

    # Verificando se os pontos estão dentro do polígono, verifica a interseção para fazer o recorte
    recortar_borda(lambda p: p[0] >= x_min, lambda p1, p2: (x_min, p1[1] + (x_min - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])))
    recortar_borda(lambda p: p[0] <= x_max, lambda p1, p2: (x_max, p1[1] + (x_max - p1[0]) * (p2[1] - p1[1]) / (p2[0] - p1[0])))
    recortar_borda(lambda p: p[1] >= y_min, lambda p1, p2: (p1[0] + (y_min - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]), y_min))
    recortar_borda(lambda p: p[1] <= y_max, lambda p1, p2: (p1[0] + (y_max - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]), y_max))
    
    return saida

# Definição da janela de recorte
x_minimo, y_minimo, x_maximo, y_maximo = 100, 100, 400, 400

# Polígonos originais
dados_poligonos = {
    "a": [(200, 200), (200, 500), (500, 200)],
    "b": [(90, 210), (230, 210), (280, 330), (160, 410), (40, 330)],
    "c": [(150, 100), (150, 150), (200, 150), (200, 200), (300, 200), (300, 150), 
          (350, 150), (350, 100), (350, 50), (300, 50), (300, 0), (200, 0), 
          (200, 50), (150, 50)],
    "d": [(120, 320), (120, 480), (380, 480), (380, 340), (300, 340), 
          (300, 410), (200, 410), (200, 320)]
}

# Aplicação do recorte
poligonos_recortados = {k: sutherland_hodgman(v, x_minimo, y_minimo, x_maximo, y_maximo) for k, v in dados_poligonos.items()}

# Plotagem
figura, eixos = plt.subplots(2, len(dados_poligonos), figsize=(15, 8))

for i, (nome, poligono) in enumerate(dados_poligonos.items()):
    eixo_original, eixo_recortado = eixos[:, i]
    
    # Polígono original
    x, y = zip(*poligono + [poligono[0]])
    eixo_original.fill(x, y, color='gray', alpha=0.5, edgecolor='black')
    eixo_original.set_title(f"Original {nome.upper()}")
    eixo_original.set_xlim(0, 500)
    eixo_original.set_ylim(0, 500)
    eixo_original.axvline(x_minimo, color='r', linestyle='--')
    eixo_original.axvline(x_maximo, color='r', linestyle='--')
    eixo_original.axhline(y_minimo, color='r', linestyle='--')
    eixo_original.axhline(y_maximo, color='r', linestyle='--')
    
    # Polígono recortado
    if poligonos_recortados[nome]:
        x_rec, y_rec = zip(*poligonos_recortados[nome] + [poligonos_recortados[nome][0]])
        eixo_recortado.fill(x_rec, y_rec, color='blue', alpha=0.5, edgecolor='black')
    eixo_recortado.set_title(f"Recortado {nome.upper()}")
    eixo_recortado.set_xlim(0, 500)
    eixo_recortado.set_ylim(0, 500)
    eixo_recortado.axvline(x_minimo, color='r', linestyle='--')
    eixo_recortado.axvline(x_maximo, color='r', linestyle='--')
    eixo_recortado.axhline(y_minimo, color='r', linestyle='--')
    eixo_recortado.axhline(y_maximo, color='r', linestyle='--')

plt.tight_layout()
plt.show()
