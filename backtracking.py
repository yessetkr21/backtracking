def movimiento_valido(matriz, x, y, visitado):
  return 0 <= x < 8 and 0 <= y < 8 and matriz[x][y] == 0 and not visitado[x][y]

def retroceder(matriz, x, y, visitado, camino):
  if x == 7 and y == 7:
      camino.append((x, y))
      print("Recorrido:")
      for nodo in camino:
          print(nodo)
      print(f"\nTotal de casillas recorridas: {len(camino)}")
      return True

  if movimiento_valido(matriz, x, y, visitado):
      visitado[x][y] = True
      camino.append((x, y))

      # Movimiento hacia arriba
      if retroceder(matriz, x - 1, y, visitado, camino):
          return True

      # Movimiento hacia abajo
      if retroceder(matriz, x + 1, y, visitado, camino):
          return True

      # Movimiento hacia la izquierda
      if retroceder(matriz, x, y - 1, visitado, camino):
          return True

      # Movimiento hacia la derecha
      if retroceder(matriz, x, y + 1, visitado, camino):
          return True

      # Retroceso si no hay movimientos válidos
      camino.pop()
      visitado[x][y] = False

  return False

def encontrar_camino(matriz):
  visitado = [[False for _ in range(8)] for _ in range(8)]
  camino = []

  print("Laberinto:")
  for fila in matriz:
      print(fila)

  if not retroceder(matriz, 0, 0, visitado, camino):
      print("No hay camino posible.")
    #implementamos ejemplos con diferentes laberintos
laberinto1 = [
  [0, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0],
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 0]
]

laberinto2 = [
]

laberinto3 = [
]

laberinto4 = [
]

encontrar_camino(laberinto1)
