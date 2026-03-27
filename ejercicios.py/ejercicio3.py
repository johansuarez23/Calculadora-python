try:
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    opcion = input("Quieres agregar un tercer numero? (s/n): ")

    if opcion == "s":
        num3 = int(input("Ingresa el tercer numero: "))
    else:
        num3 = None

    # Empezamos desde el número mayor
    if num3:
        mayor = max(num1, num2, num3)
    else:
        mayor = max(num1, num2)

    while True:
        if num3:
            if mayor % num1 == 0 and mayor % num2 == 0 and mayor % num3 == 0:
                print("El MCM es:", mayor)
                break
        else:
            if mayor % num1 == 0 and mayor % num2 == 0:
                print("El MCM es:", mayor)
                break

        mayor += 1

except ValueError:
    print("Debes ingresar solo números")
