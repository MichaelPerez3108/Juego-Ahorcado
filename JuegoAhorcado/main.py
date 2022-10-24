from Funciones import *
def main():
  palabra = seleccionarpalabra()
  alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
  jugada = ["_"]*len(palabra)

  for turno in range(5):
    print(f"\nTurno: {turno+1}")
    print("-"*20)
    #imprimir alfabeto y jugada
    imprimiractualizacion(alfabeto,jugada)
    #entrada usuario
    letra = entradausuario()
    #actualizar jugada y alfabeto
    jugada = actualizarjugada(palabra,letra,jugada)
    alfabeto = actualizaralfabeto(letra,alfabeto)
    #imprimir actualizacion
    imprimiractualizacion(alfabeto,jugada)
    #preguntar al usuario si desea adivinar o no la palabra
    check = input("Desea adivinar la palabra? (S/N): ")
    if check.lower() == "s":
      suposicion = input("Introduzca su respuesta: ").lower()
      success = verificarjugada(suposicion,palabra)

      if success:
        print("+"*20)
        print("SIU GANASTE")
        print("+"*20)
      break
  else:
      print("+"*20)
      print("La suposicion es incorrecta...")
      print("+"*20)
  if turno == 4:
    print("-"*20)
    print("=( =( AHORCADOOOOOOO")
    print("-"*20)
if __name__ == "__main__":
  main()