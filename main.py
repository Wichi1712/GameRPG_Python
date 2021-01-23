from personajes import Jugador, Soldado, Arquero, Espadachin, EnemigoPrueba
#import control
from control import combate, recompensa, limpiarPantalla
from random import randint

#propiedades de personaje
jugador = Jugador("nombre", 100, 50, "respuesta")

#nombrePersonaje = ""
#energiaJugador = 100
#respuestaPersonaje = ""
#ataquePersonaje = 100

#Enemigos
#soldado = Enemigo("soldado", 100, 5)
#arquero = Enemigo("Arquero", 50, 10)
#espadachin = Enemigo("Espadachin", 150, 15)


print("Hola Bienvenido este es un juego RPG")
jugador.nombre = input("Por favor ingresa tu nombre:\n")
print("Hola tu nombre es: " + jugador.nombre)
print("Tu salud es: " + str(jugador.salud))


print("-------------Comienza el juego----------------------------")

#Nivel 1 de enemigos
nivelEnemigoPrueba = 3
nivel1 = [Soldado(),Arquero(),Soldado(),Espadachin()]
nivel2 = [EnemigoPrueba(nivelEnemigoPrueba), EnemigoPrueba(randint(1,5))]

for enemigo in nivel1:
  combate(jugador,enemigo)
  recompensa(jugador)
  limpiarPantalla()

#combate(jugador, soldado)
#recompensa(jugador)
#print("-------NUEVO ENEMIGO--------")
#combate(jugador, arquero)

print("¡BIEN! Superaste el primer nivel")


for enemigo in nivel2:
  combate(jugador,enemigo)
  recompensa(jugador)
  limpiarPantalla()
