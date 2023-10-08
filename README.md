# Proyecto 2 - Compiladores - Generacion de codigo intermedio

## Estructuración del proyecto

- CodigoIntermedio.md
- main.py
- threeAddressCode.py
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

## build/yaplWalker.py

Este código define un visitante para árboles de análisis generados por el parser de yapl. El visitante está estructurado para manejar y visitar diferentes tipos de nodos en el árbol.

Importaciones:

Importa herramientas necesarias de antlr4.
Se condiciona la importación del módulo yaplParser dependiendo de si el archivo actual se ejecuta como módulo o no.

Clase yaplVisitor:

Hereda de ParseTreeVisitor.
Esta clase define un visitante genérico completo para un árbol de análisis producido por yaplParser.

Métodos de Visitante:

Cada método de visitante tiene un patrón similar: visit[NombreDelNodo](self, ctx).
Por ejemplo, visitProg, visitClass_def, visitFeat_def, etc.
Cada método visita un nodo específico (o tipo de nodo) en el árbol de análisis.
Todos los métodos actualmente simplemente llaman a self.visitChildren(ctx), que visita todos los nodos hijos del nodo actual.

Eliminación de yaplParser:

Al final del archivo, el código elimina la referencia a yaplParser con del yaplParser.

## yaplWalker.py

El propósito de la clase yaplWalker es recorrer el Árbol de Sintaxis Abstracta (AST) generado por el analizador YAPL y realizar diversas acciones y validaciones, como poblar una tabla de símbolos y generar código de tres direcciones.

Aquí hay un resumen de los diversos componentes y funcionalidades proporcionadas por la clase yaplWalker:

Inicialización y Propiedades:

Inicializa una serie de variables de instancia como labels, basic_types, contadores para main_class y main_method, current_class_name y current_class_uuid, entre otros.
Tabla de Símbolos y Código de Tres Direcciones (TAC):

Las funciones initSymbolTable e init3AddressCode para inicializar la tabla de símbolos y TAC, respectivamente.
getSymbolTable y getTAC para recuperarlos.
add_to_symbol_table agrega entradas a la tabla de símbolos y maneja posibles errores.

Funciones de Utilidad:

find_type_id y find_object_id: Recuperan símbolos de la tabla de símbolos basándose en su ID.
new_label: Crea y devuelve una nueva etiqueta para el código de tres direcciones.
Funciones Visitantes: Las dos principales funciones visitantes son:

visitProg: Esta función visita el nodo raíz del AST. Primero define las clases básicas (Object, Int, Bool, String y IO) y sus métodos. Luego, visita a sus hijos. Después del recorrido, verifica si hay exactamente una clase principal y un método principal.

visitClass_def: Esta función visita los nodos de definición de clases. Valida la clase (verificando si la clase hereda correctamente y asegura que no haya múltiples herencias o herencias recursivas). Si las validaciones pasan, añade la clase a la tabla de símbolos.
Hay múltiples verificaciones de errores en todo el código. Por ejemplo, verifica:

La existencia de solo una clase Main.
Solo un método principal en la clase Main.
Validaciones de herencia de clases (por ejemplo, una clase no debe heredar de un tipo básico, o de sí misma, y no se permite la herencia múltiple).

visitFeat_def:

Establece el nombre del método actual que se está procesando.
Verifica si hay demasiados métodos principales denominados "main" y si el método principal tiene parámetros formales, lo cual no es permitido.
Busca el símbolo en la tabla de símbolos y agrega errores si se encuentra que ya existe.
Si no existe, agrega el símbolo a la tabla y genera código de tres direcciones para visitar la expresión dentro del método.

visitFeat_asgn:

Busca una variable en la tabla de símbolos dentro del alcance local y verifica si ya existe. Si es así, agrega un error. Si no, la añade a la tabla de símbolos.
Visita los hijos del nodo.
visitFormal:

Establece el alcance global y local.
Busca el símbolo del método en la tabla de símbolos y agrega los tipos de parámetros al símbolo.
Verifica si el parámetro ya existe dentro del alcance actual. Si es así, agrega un error.
Añade el parámetro a la tabla de símbolos y visita los hijos del nodo.
visitAsgn:

Es una función vacía en este fragmento y simplemente devuelve el contexto.

visitExpr_asgn:

Busca el símbolo de la variable en los alcances local y global y genera código de tres direcciones para asignar un valor a la variable.

visitExpr_class_call:

Visita las expresiones dentro de la llamada y genera código de tres direcciones para la llamada de clase.

visitExpr_call:

Visita las expresiones dentro de la llamada y genera código de tres direcciones para la llamada al método.

visitExpr_if:

Genera código de tres direcciones para una estructura condicional "if-else" basado en las expresiones proporcionadas.

visitExpr_while:

Genera código de tres direcciones para una estructura de bucle "while" basado en las expresiones proporcionadas.

visitExpr_brackets:

Visita las expresiones dentro de los corchetes y devuelve la primera expresión.

visitExpr_decl:
Visita la declaración de expresión y genera código de tres direcciones para la declaración.

visitExpr_instance: Este método visita la parte del árbol que maneja expresiones de instancia. Parece que está generando una nueva instancia de un tipo. Se crea un terceto (código de tres direcciones) con el identificador del tipo.

visitExpr_isvoid: Este método maneja la expresión isvoid. Verifica si el valor de una expresión es nulo o no.

visitExpr_suma: Este método es responsable de las operaciones de suma (adición) y resta. Determina si la operación es suma o resta y luego calcula el resultado.

visitExpr_mult: Este método es para operaciones de multiplicación y división. De manera similar al método de suma, determina el tipo de operación y luego calcula el resultado.

visitExpr_negative: Maneja la expresión negativa, multiplicando efectivamente el valor de la expresión por -1.

visitExpr_negado: Este método niega el valor de la expresión.

visitExpr_less_than: Este método maneja las operaciones menor que (<) y menor o igual a (<=).

visitExpr_equal: Este método verifica si dos expresiones son iguales.

visitExpr_not: Este método realiza una operación lógica NOT en una expresión.

visitExpr_parenthesis: Parece ser para manejar expresiones encerradas entre paréntesis. La operación real que se realiza no está del todo clara en el código proporcionado.

visitExpr_id: Este método busca identificadores, que podrían ser un tipo o un objeto.

visitExpr_int: Maneja valores enteros.

visitExpr_str: Maneja valores de cadena.

visitExpr_true: Devuelve un valor booleano verdadero.

visitExpr_false: Devuelve un valor booleano falso.

visitExpr_self: Devuelve la cadena "self", que probablemente se refiere a la instancia actual de un objeto en un contexto orientado a objetos.
