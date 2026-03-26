try:
    num1 = float(input("primer numero: "))
    num2 = float(input("segundo numero: "))
    num3 = float(input("tercer numero: "))
except ValueError:
    print (" Ese no es un numero ")
    exit()
operacion = input (" Elige: +, -, *, / : ")
if operacion == "+":
    print(num1 + num2 + num3)
elif operacion == "-":
    print(num1 - num2 - num3)
elif operacion == "/":
    if num2 == 0 or num3 == 0:
        print("no se puede dividir por 0")
    else:
        print(num1 / num2 / num3)
        
elif operacion == "*":
    print(num1 * num2 * num3)
else:
    print("operacion no valida")

  
    