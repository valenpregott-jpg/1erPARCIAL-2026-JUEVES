## Ejercicio 1: La Serie de Potencias de Homero

Generar una lista por compresión que contenga la cantidad de donas que Homero consume en el infierno. 
Por cada dona que Homero consume apareceran más donas al ritmo de raíz de dos donas ($\displaystyle \sqrt{2}$) en su suplicio hasta que reviente.  

Ejemplo: <code>{ 1: 1, 2: 1.41421356237, 3: 2, 4: 2.82842712475, 5: ... }</code>




import math
n = 10 
donas= [math.sqrt(2)] ** (k-1) for k in range(1, n + 1)]
print(donas)