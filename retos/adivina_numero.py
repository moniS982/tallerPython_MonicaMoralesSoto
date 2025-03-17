import random
if __name__ == '__main__':
    i: int = 0
    nuRandom = random.randint(1,100)
    bol = False
    while bol == False and i<10:
        try:
            y = int(input("Ingresa un numero entero entre 1 y 100: "))
            if y >= 1 and y <= 100:
                i += 1
                if y < nuRandom:
                    print("El numero a divinar es mayor")
                else:
                    if y > nuRandom:
                        print("El numero a adivinar es menor")
                    else:
                        if y == nuRandom:
                            print("Felicidades has acertado el numero")
                            print(f"Lo lograste en el intento numero : {i} ")
                            bol = True
                if i==10:
                    print(f"No tienes mas intentos. El numero era {nuRandom}")
            else:
                print("Debe estar en el rango entre 1 y 100")
                print("Intentalo nuevamente")

        except ValueError:
            print("Ingrese un numero entero")


