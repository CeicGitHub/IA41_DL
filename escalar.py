import tensorflow as tf

escalar = tf.constant(7)
print(escalar)
print("Dimensiones:", escalar.ndim)


vector = tf.constant([2, 4, 6, 8])
print(vector)
print("Dimensiones:", vector.ndim)


matriz = tf.constant([[1, 2, 3],
                      [4, 5, 6]])
print(matriz)
print("Dimensiones:", matriz.ndim)

tensor3D = tf.constant([
    [[1, 2], [3, 4]],  # "capa" 1
    [[5, 6], [7, 8]]   # "capa" 2
])
print(tensor3D)
print("Dimensiones:", tensor3D.ndim)


tensor4D = tf.random.normal([32, 28, 28, 3])
print("Forma:", tensor4D.shape)
print("Dimensiones:", tensor4D.ndim)


| Función | Código en TensorFlow |
| ------- | -------------------- |
| Sigmoid | `tf.nn.sigmoid(x)`   |
| Tanh    | `tf.nn.tanh(x)`      |
| ReLU    | `tf.nn.relu(x)`      |


x = tf.constant([-1.0, 2.0, 0.0, 4.0])


tf.nn.sigmoid(x)
tf.nn.tanh(x)
tf.nn.relu(x)
tf.tensordot(x, x, axes=1)  # Producto punto

#! FUNDAMENTOS DE ELECTRONICA DIGITAL:
 #?1) Algebra Boolena: AND, OR, NOT, NAND, NOR, XOR, XNOR
 #?2) Mapas de Karnaugh
 #?3) Teoremas de De Morgan
 #?4) Circuitos Combinacionales y Secuenciales: Flip-Flops, Contadores, Registros
 #?5) Sistemas de Numeración: Binario, Decimal, Hexadecimal, Octal, Complemento a 2
 #?6) Aritmética Binaria: Suma, Resta, Multiplicación, División
 #?7) FSM --> Maquinas de Estados Finitos

#! Arquitectura de Computadoras y Diseño Digital:
#? Bus de Datos y Direcciones
#? Unidad de Control
#? ALU (Unidad Aritmético-Lógica)
#? Memoria y Registros
#? Jerarquía de Memoria: Caché, RAM, ROM
#? Ciclos de Instrucción o Reloj

#! Verilog:
#? "assign", bloques "always", (always @ (*)) y (always @ (posedge clk))
#? Tipos de Datos: wire, reg, integer
#? Operadores: Aritméticos, Lógicos, Relacionales, Bit a Bit
#? Estructuras de Control: if-else, case
#? Módulos y Puertos

#todo: Instalar en Visual Studio Code la extensión de Verilog-HDL/SystemVerilog
#todo: Instalar Quartus Prime Lite Edition 18.1


