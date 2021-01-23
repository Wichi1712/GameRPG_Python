from random import randint

def combate(player, enemy):

  while player.estaVivo and enemy.estaVivo:
    print("")

    print("El enemigo "+ enemy.nombre + " te ataca con fuerza de: " + str(enemy.ataque))
    player.pierdeEnergia(enemy.ataque)
    print("Ahora tu salud es " + str(player.salud))
    print("")

    respuestaPersonaje = input("¿Que accion quieres tomar?\n a) Atacar ==> " + "Valor de tu ataque: " + str(player.ataque) + "\n m) Mostrar salud de " + enemy.nombre + ":\nIngrese accion: ")

    if respuestaPersonaje == "a":
      print("Atacas al enemigo " + enemy.nombre + " con una fuerza de " + str(player.ataque))
      enemy.pierdeEnergia(player.ataque)
      print("Ahora el enemigo " + enemy.nombre + " tiene " + str(enemy.salud) + " de salud")
      print("El nivel del enemigo " + enemy.nombre + " es: " + str(enemy.nivel))
      if enemy.estaVivo == False:
        break
    elif respuestaPersonaje == "m":
      print("El enemigo " + enemy.nombre +" tiene " + str(enemy.salud) + " de salud")

  print("")
  print("Tu salud es: " + str(player.salud))
  #print("Has sido derrotado por el " + enemy.nombre)

  print("La salud del enemigo " + enemy.nombre + " es: " + str(enemy.salud))

  print("Bien derrotaste al enemigo: " + enemy.nombre + "\n")


def recompensa(personaje):
  p = randint(1,3)
  if p == 1:
    print("Recuperas salud +10")
    personaje.salud += 10
  elif p == 2:
    print("Obtienes +10 de experiencia")
    personaje.experiencia += 10
  elif p == 3:
    print("Obtienes amuleto de fuerza +10")
    personaje.ataque += 10


def limpiarPantalla():
	print('\n'*3 + "-------NUEVO ENEMIGO--------")