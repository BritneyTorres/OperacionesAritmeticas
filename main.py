def gcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros a y b utilizando el algoritmo de Euclides.

    Parámetros:
        a (int): El primer número entero.
        b (int): El segundo número entero.

    Retorna:
        int: El máximo común divisor (MCD) de a y b.
    """
    while b:
        a, b = b, a % b
    return a


# Función para validar la entrada del usuario
def obtener_numero_positivo(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num <= 0:
                print("Por favor, ingrese un número entero positivo mayor que cero.")
            else:
                return num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")


# Solicitar al usuario que ingrese los números
num1 = obtener_numero_positivo("Ingrese el primer número entero positivo mayor que cero: ")
num2 = obtener_numero_positivo("Ingrese el segundo número entero positivo mayor que cero: ")

# Calcular y mostrar el máximo común divisor
print("El máximo común divisor de", num1, "y", num2, "es:", gcd(num1, num2))
