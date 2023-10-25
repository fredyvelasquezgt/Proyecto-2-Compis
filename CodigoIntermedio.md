# Diseño código intermedio

El código de tres direcciones está diseñada para la evaluación de operaciones aritméticas y tiene la forma: 
$$
x = y \text{ op } z
$$

## Proposiciones
Las propociciones que pueden existir en nuestro codigo de tres direcciones son:
  * Asignaciones Binarias
    * $a = b \text{ op } c$
  * Asignaciones Unarias
    * $a = -b$
  * Instrucciones de copia por valor
    * $a=b$
  * Instrucciones de copia por referencia
    * $a = c[b]$
    * $c[b] = a$
  * Saltos incondicionales
    * $\text{ goto } B1$
  * Saltos condicionales
    * $if(a) \text{ goto } B1$
    * $if(a<b)  \text{ goto } B1$
    * $if(a<b or c>d)  \text{ goto } B1$
    * Nota: misma manera para ciclos while y for
  * Llamadas a funciones
    * $\text{ call } funcion(a, b, ...n)$
    * $a = \text{ call } funcion(a, b, ...n)$


## Estructura de dato
Aunque se suele utilizar la estructura de un cuarteto para la implementación de código de tres direcciones, esta ocupa mucho espacio y se necesita el uso de muchas variables temporales para realizar los calculos intermedios. Es por eso que se utilizará la estructura de un *terceto*. 
<br>
A diferencia del cuarteto que su estructura es $(op, a, b, res)$ en donde:
* $op$ = operador
* $a$ = argumento 1
* $b$ = argumento 2
* $res$ = resultado

El terceto utiliza únicamente la estructura $(op, a, b)$ ya que el resultado está implícito en el terceto. Los tercetos referencian a otros tercetos donde está el resultado que necesitan para operar. Por ejemplo:
<br>
$x = y + z - (a * b)$

|No.|Transformacion   |Terceto    |
|---|-----------------|-----------|
| 1 |temp1 = a * b    |(*, a, b)  |
| 2 |temp2 = z - temp1|(-, z, (1))|
| 3 |temp3 = y + temp2|(+, y, (2))|
| 4 |x = temp3        |(=, (3), x)|    



## Tamaño tipos de datos básicos
|Tipo  |Tamaño en bytes|
|------|-------------- |
|int   |8              |
|bool  |1              |
|string|1 por caracter |



 