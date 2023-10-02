from turtle import *
import random
import os

window = Screen()
window.bgcolor("black")
random_angles = [30, 60]

def dibujarArbol(tamanoDeRama, tortuga, continuar):
    random_angle = random.choice(random_angles)
    tortuga.pensize(tamanoDeRama/30)
    if (tamanoDeRama < 30):
        return
        if(continuar == False):
            tortuga.forward(tamanoDeRama)
            tortuga.left(random_angle)
            dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
            tortuga.right(random_angle*2)
            dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
            tortuga.left(random_angle)
            tortuga.backward(tamanoDeRama)
    tortuga.forward(tamanoDeRama)
    tortuga.left(random_angle)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
    tortuga.right(random_angle*2)
    dibujarArbol(tamanoDeRama*random.uniform(0.8, 0.9), tortuga, continuar)
    tortuga.left(random_angle)
    tortuga.backward(tamanoDeRama)

def dibujarNuevoArbol(continuar):
    tortuga = Turtle()
    tortuga.speed(0)
    tortuga.left(90)
    tortuga.penup()
    tortuga.setpos(0, -300)
    tortuga.pendown()
    tortuga.hideturtle()
    tortuga.color("#ffffff")
    dibujarArbol(100, tortuga, continuar)

if __name__ == '__main__':
    while True:
        os.system('cls')
        respuesta = input("¿Quieres dibujar otro árbol? (S/N) o si quieres salir (E): ").strip().lower()
        if respuesta == 'n':
            dibujarNuevoArbol(True)
        if respuesta == 's':
            window.reset()  # Limpia la ventana
            dibujarNuevoArbol(False)
        if (respuesta == 'e'):
            print("Puedes darle click a la pantalla para salir")
            window.exitonclick()
            break
