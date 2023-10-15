import turtle as t
import random, os, pyautogui, csv


window = t.Screen()
window.bgcolor("black")
random_angles = [30, 60]
coordenadas_guardadas = []

def dibujarArbol(tamanoDeRama, tortuga, continuar):
    random_angle = random.choice(random_angles)
    # random_angle = random.randint(0,360)
    tortuga.pensize(tamanoDeRama/30)
    if tamanoDeRama < 30:
        return
        if not continuar: # asumiendo que `continuar` es un booleano
            tortuga.forward(tamanoDeRama)
            print(tortuga.pos())
            tortuga.left(random_angle)
            dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
            tortuga.right(random_angle*2)
            dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
            tortuga.left(random_angle)
            tortuga.backward(tamanoDeRama)
    tortuga.forward(tamanoDeRama)
    coordenadas_guardadas.append(tortuga.pos())
    # print(coordenadas_guardadas)
    tortuga.left(random_angle)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
    tortuga.right(random_angle*2)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
    tortuga.left(random_angle)
    tortuga.backward(tamanoDeRama)

def dibujarNuevoArbol(continuar):
    tortuga = t.Turtle()
    tortuga.speed(0)
    tortuga.left(90)
    tortuga.penup()
    tortuga.setpos(0, -250)
    tortuga.pendown()
    tortuga.hideturtle()
    tortuga.color("#ffffff")
    dibujarArbol(100, tortuga, continuar)

if __name__ == '__main__':
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Ésto lo vuelve compatible con Linux y macOS
        respuesta = input("¿Quieres dibujar otro árbol? (S/N) o si quieres salir (E) (Screenshot=>'d') (Leer un archivo .csv => 'l'): ").strip().lower()
        if respuesta == 'n':
            dibujarNuevoArbol(True)
        elif respuesta == 's':
            window.reset()  # Limpia la ventana
            dibujarNuevoArbol(False)
            nombre_archivo = "datos_arbol.csv"

            # Abre el archivo CSV en modo de escritura
            with open(nombre_archivo, "w", newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv, delimiter=",")
                # Escribe los datos en el archivo CSV
                for x, y in coordenadas_guardadas:
                    escritor_csv.writerow([x, y])

            print(f"Los datos han sido guardados en '{nombre_archivo}'.")
        elif respuesta == 'l':
            window.reset()  # Limpia la ventana
            with open("datos_arbol.csv", "r", newline="")as archivo_csv:
                # Crea un objeto reader para leer los datos
                # Usa el parámetro quotechar para indicar el paréntesis
                reader = csv.reader(archivo_csv)
                # Crea una lista vacía para almacenar las coordenadas
                coordenadas2 = []
                # Lee cada fila y convierte los valores a números
                for row in reader:
                    x = float(row[0])
                    y = float(row[1])
                    # Añade la coordenada a la lista
                    coordenadas2.append((x, y))
            lector_csv = csv.DictReader(coordenadas2)
            lapiz = t.Turtle()
            lapiz.color("#ffffff")
            for x, y in coordenadas2:
                lapiz.goto(x, y)
        elif respuesta == 'e':
            print("Puedes darle click a la pantalla para salir")
            window.exitonclick()
            break
        elif respuesta=='d':
            screenshot = pyautogui.screenshot()
            # Directorio donde guardar las capturas de pantalla
            directorio = "images/"
            # Crear el directorio si no existe
            if not os.path.exists(directorio):
                os.makedirs(directorio)
            # Variable para mantener un contador
            contador = 1
            while True:
                # Comprobar si el archivo ya existe
                nombre_archivo = f"captura_{contador}.png"
                if os.path.exists(os.path.join(directorio, nombre_archivo)):
                    contador += 1
                else:
                    # Tomar una nueva captura de pantalla
                    # Especifica el título de la ventana que deseas capturar
                    ventana_especifica = "Python Turtle Graphics"

                    # Obtén las coordenadas (x, y) y dimensiones (ancho, alto) de la ventana
                    ventana_info = pyautogui.getWindowsWithTitle(ventana_especifica)[0]
                    x, y, ancho, alto = ventana_info.left, ventana_info.top, ventana_info.width, ventana_info.height

                    # Recorta la captura de pantalla para incluir solo la ventana específica
                    captura_recortada = screenshot.crop((x, y, x + ancho, y + alto))
                    ruta_completa = os.path.join(directorio, nombre_archivo)
                    captura_recortada.save(ruta_completa)
                    print(f"Captura guardada como {ruta_completa}")
                    contador += 1
                    seguir = input("¿Quieres tomar otra captura de pantalla? (s/n): ")
                    if seguir.lower() != "s":
                        break