class Enemigo:
  def __init__(self, nombre, salud, ataque, nivel):
    self.nombre = nombre
    self.salud = salud
    self.ataque = ataque
    self.estaVivo = True
    self.nivel = nivel

  
  def pierdeEnergia(self, cantidad):
    if self.estaVivo:
      self.salud -= cantidad
      if self.salud <= 0:
        self.estaVivo = False


class Soldado(Enemigo):
  def __init__(self):
    super().__init__("Soldado", 100, 5, 1)
  

class Arquero(Enemigo):
  def __init__(self):
    super().__init__("Arquero", 50, 10 , 1)

class Espadachin(Enemigo):
  def __init__(self):
    super().__init__("Espadachin", 150, 15, 1)



#---PRUEBA DE ENEMIGO---------------

class Enemigo2:
  def __init__(self, nombre, salud, ataque, nivel):
    self.nombre = nombre
    self.salud = salud
    self.ataque = ataque
    self.estaVivo = True
    self.nivel = nivel

  
  def pierdeEnergia(self, cantidad):
    if self.estaVivo:
      self.salud -= cantidad
      if self.salud <= 0:
        self.estaVivo = False

class EnemigoPrueba(Enemigo2):
  def __init__(self, nivel):
    super().__init__("EnemigoPrueba", 200, 20, nivel)

#---------------------------------------

class Jugador:
  def __init__(self, nombre, salud, ataque, respuesta):
    self.nombre = nombre
    self.salud = salud
    self.ataque = ataque
    self.respuesta = respuesta
    self.estaVivo = True
    self.experiencia = 0

  def pierdeEnergia(self, cantidad):
    if self.estaVivo:
      self.salud -= cantidad
      if self.salud <= 0:
        self.estaVivo = False