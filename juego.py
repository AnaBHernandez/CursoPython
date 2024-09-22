import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinando =False

    print("¡Bienvenid@ al juego de adivinanzas de números!")
    print("@Dime un número entre 1 y 100")

    while not adivinando:
        intento = int(input("Adivina el número:"))
        intentos += 1
        if intento < numero_secreto:
            print("El número correcto es mayor")
        elif intento > numero_secreto:
            print("El número correcto es menor")
        else:
            adivinando = True
            print(f"!Felicidades¡ Adivinaste en {intento} intentos")               
juego_adivinanza()    

