# Proyecto 2 - Compiladores - Generacion de codigo intermedio

## Estructuración del proyecto

- CodigoIntermedio.md:
- main.py:
- threeAddressCode.py:
- yaplWalker.py

## CodigoIntermedio.md

El documento proporciona una guía sobre cómo se diseñan y estructuran operaciones aritméticas intermedias, describiendo los tipos de proposiciones que se pueden representar y detallando las estructuras de datos utilizadas en el proceso.

## main.py

Importación de Módulos:

Se importan varias bibliotecas y módulos para realizar operaciones específicas como GUI, procesamiento de archivos, análisis léxico y sintáctico, entre otros.
Definición de la Clase YaplAnalyzerApp:

Esta clase principal maneja toda la lógica y diseño de la interfaz gráfica.
Constructor __init__:

Se inicializa la ventana principal, se configura el título, el tamaño y el color de fondo.
Se crean y configuran los widgets de la interfaz gráfica.
create_widgets():

Método que define y organiza los componentes de la ventana principal, como botones, áreas de texto y barras de desplazamiento.
open_file():

Método que permite al usuario seleccionar un archivo para abrir y leer su contenido, mostrándolo en una de las áreas de texto.
run_analysis():

Este método se encarga de tomar el contenido del área de texto, guardarlo temporalmente en un archivo y posteriormente analizarlo léxica, sintáctica y semánticamente.
clear_text_areas() y clear_output_text_areas():

Estos métodos borran el contenido de las áreas de texto.
analyze_code():

Se lleva a cabo el análisis real del código utilizando ANTLR (un generador de analizadores) para realizar el análisis léxico y sintáctico. Los errores léxicos, sintácticos y semánticos se muestran en una consola dentro de la GUI.
display_errors():

Muestra errores específicos en el área de la consola.
display_tac():

Muestra el código de tres direcciones (TAC) generado a partir del análisis.
view_all() y LineNumbers:

view_all() se encarga de sincronizar el desplazamiento vertical entre el área de texto y el área de números de línea.
LineNumbers es una subclase para mostrar los números de línea junto al área de texto donde se muestra el código.
Ejecución Principal:

Si este archivo se ejecuta como un script principal, se crea una instancia de la clase YaplAnalyzerApp y se inicia la GUI.

## threeAddressCode.py

Clase Terceto:

Atributos: Define componentes de una instrucción de tres direcciones: operador (o), operandos (x y y), resultado (r), y etiqueta (l). Es evidente que hay partes del código que no utilizan el atributo r (comentado).
Método keys(): Devuelve una lista de las claves que representan los atributos de un terceto. Hay código redundante y posiblemente errores ya que hay dos declaraciones return.
Método values(): Devuelve una lista de los valores asociados a un terceto, nuevamente hay código redundante con dos declaraciones return.

Clase ThreeAddressCode:

Atributo tercetos: Una lista que almacenará los tercetos creados.
Método add(): Permite agregar un nuevo terceto a la lista. Valida y convierte los valores de entrada a cadenas si no son None, enteros o cadenas. También genera un valor predeterminado para el atributo r si no se proporciona.
Método generate_code(): Genera y escribe el código intermedio basado en los tercetos en un archivo llamado "output/code.tac". Según el operador y los operandos, decide qué formato de instrucción escribir.
