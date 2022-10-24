import random
# funcion para escoger una palabra random
def seleccionarpalabra():
  lineas = open("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra


# Funcion entrada del teclado
def entradausuario():
  letra = input("Introduzca una letra: ")
  return letra.lower()
# funcion actualizar jugada
def actualizarjugada(palabra, letra, jugada):
  n_letras = len(palabra)

  for i in range (0, n_letras,):
    if palabra[i] == letra:
      jugada[i] = letra
    
  return jugada




# funcion para actualizar el alfabeto
def actualizaralfabeto(letra, alfabeto):
  alfabeto = alfabeto.replace(letra, " ")
  return alfabeto

# imprimir resultado de la jugada en pantalla
def imprimiractualizacion(alfabeto,jugada):
  print(f"Jugada: {jugada}")
  print(f"Letras disponibles: {alfabeto}")

#verificar la jugada con la palabra que se esta jugando
def verificarjugada(suposicion,palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success
