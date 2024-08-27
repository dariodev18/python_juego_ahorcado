import random


def obtener_palabra_secreta() -> str:
    palabras = ['Python','Javascript','java','Django','tensorflow','react','typescript','git','flask']
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta,letras_adivinadas):
    adivinado = ''
    
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
            
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta().lower()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    
    print("Bienvenidos al juego del ahorcado!")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta,letras_adivinadas), "la cantidad de letras de la palabra es:", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()
        
        if len(adivinanza) !=1 or not adivinanza.isalpha():
            print("Debes introducir una letra")
        elif adivinanza in letras_adivinadas:
            print("Ya has introducido esa letra, intenta con otra")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"Has acertado, la letra '{adivinanza}' esta presente el la palabra")
            else:
                intentos -= 1
                print(f"La letra '{adivinanza}' no esta presente en la palabra")
                print(f"Te quedan '{intentos}' intentos")
                
        progreso_actual = mostrar_progreso(palabra_secreta,letras_adivinadas)
        print(progreso_actual)
        
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"Has ganado, la palabra secreta era '{palabra_secreta}'" )
    
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Has perdido, la palabra secreta era {palabra_secreta}")

juego_ahorcado()