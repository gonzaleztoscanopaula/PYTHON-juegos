import random


def elegir_opcion():
  opciones = ('piedra', 'papel', 'tijera')
  usuario_opcion = input('piedra, papel o tijera => ')
  usuario_opcion = usuario_opcion.lower()

  if not usuario_opcion in opciones:
    print('Esa opcion no es valida')
    return None, None

  pc_opcion = random.choice(opciones)

  print('Opcion del usuario: ', usuario_opcion)
  print('Opcion de la PC: ', pc_opcion)
  return usuario_opcion, pc_opcion

def reglas(usuario_opcion, pc_opcion, usuario_gana, pc_gana):
  if usuario_opcion == pc_opcion:
    print('Empate!')
  elif usuario_opcion == 'piedra':
    if pc_opcion == 'tijera':
      print('piedra gana a tijera')
      print('Tú ganas!')
      usuario_gana += 1
    else:
      print('Papel gana a piedra')
      print('PC gano!')
      pc_gana += 1
  elif usuario_opcion == 'papel':
    if pc_opcion == 'piedra':
      print('papel gana a piedra')
      print('Tú ganas')
      usuario_gana += 1
    else:
      print('tijera gana a papel')
      print('PC gano!')
      pc_gana += 1
  elif usuario_opcion == 'tijera':
    if pc_opcion == 'papel':
      print('tijera gana a papel')
      print('Tú ganas!')
      usuario_gana += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      pc_gana += 1
  return usuario_gana, pc_gana

def iniciar_juego():
  pc_gana = 0
  usuario_gana = 0  
  rondas = 1
  while True:
    print('*' * 10)
    print('Ronda: ', rondas)
    print('*' * 10)

    print('PC : ', pc_gana)
    print('Usuario: ', usuario_gana)
    rondas += 1

    usuario_opcion, pc_opcion = elegir_opcion()
    usuario_gana, pc_gana = reglas(usuario_opcion, pc_opcion, usuario_gana, pc_gana)

    if pc_gana == 2:
      print('El ganador es la PC, se te rie en la cara Bill Gates')
      break

    if usuario_gana == 2:
      print('Podrás vencer a una computadora, pero no al sistema maldito peón')
      break

iniciar_juego()