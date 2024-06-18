def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

while True:
    lado1 = float(input("Digite o comprimento do primeiro lado: "))
    lado2 = float(input("Digite o comprimento do segundo lado: "))
    lado3 = float(input("Digite o comprimento do terceiro lado: "))

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print("É possível formar um triângulo.")
        print("Tipo de triângulo:", tipo_triangulo(lado1, lado2, lado3))
        break
    else:
        print("Não é possível formar um triângulo com esses comprimentos. Tente novamente.")