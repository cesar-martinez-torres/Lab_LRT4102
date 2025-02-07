class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

# Solicitar los números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Crear un objeto de la clase Calculadora
calculadora = Calculadora(num1, num2)

# Realizar la suma e imprimir el resultado
print(f"La suma de {num1} y {num2} es {calculadora.sumar()}")

