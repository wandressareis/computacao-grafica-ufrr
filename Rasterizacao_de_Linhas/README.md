## Rasterização de Linhas com os Algoritmos Analítico, Analisador Diferencial Digital e Bresenham

Desenho de retas por meio dos algoritmos de raterização linear: Analítico, Analisador Diferencial Digital (DDA)  e Bresenham.

## Algoritmo Analítico

---

O **método analítico** utiliza uma abordagem simples e intuitiva para determinar a equação de uma reta a partir de dois pontos. O procedimento é descrito a seguir:

### Passos do Algoritmo:

O método usado pelo algoritmo analítico é o mais simples e intuitivo, que consiste em:

   - Dados os extremos P_1(x_1, y_1) \ e \ P_2(x_2, y_2)

- Descobre a equação reduzida da reta \( y = mx + b \):
  - O coeficiente angular \( m \)é dado por:

  $$
  m = \frac{y_2 - y_1}{x_2 - x_1}
  $$
  
  - O coeficiente linear \( b \) pode ser encontrado por:
  
  $$
  b = y_1 - m \cdot x_1
  $$

Portanto, a equação reduzida da reta será:

$$
y = m \cdot x + b
$$

---
<div style="text-align:center">

  <img src="./src/analitico1.png" alt="Alt text"  width="200"/>

  <img src="./src/analitico2.png" alt="Alt text" width="200"/>

  <img src="./src/analitico_vertical.png" alt="Alt text" width="200"/>

  <img src="./src/analitico_horizontal.png" alt="Alt text" width="200"/>

</div>

### Algoritmo Analisador Diferencial Digital (DDA)


<div style="text-align:center">

  <img src="./src/dda1.png" alt="Alt text"  width="200"/>

  <img src="./src/dda2.png" alt="Alt text" width="200"/>

  <img src="./src/dda_vertical.png" alt="Alt text" width="200"/>

  <img src="./src/dda_horizontal.png" alt="Alt text" width="200"/>
  
</div>

### Algoritmo Bresenham


<div style="text-align:center">

  <img src="./src/bresenham1.png" alt="Alt text"  width="200"/>

  <img src="./src/bresenham2.png" alt="Alt text" width="200"/>

  <img src="./src/bresenham_vertical.png" alt="Alt text" width="200"/>

  <img src="./src/bresenham_horizontal.png" alt="Alt text" width="200"/>
  
</div>
