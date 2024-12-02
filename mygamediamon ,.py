import random

car = r'''       
         __________________________
        /   | |______| |___     __/ 
       /  , | |  /\  | | ^ |   |       ,--.  
     ,' ,'| | |.'  `.| |/ \|   |      /    \  
   ,' ,'__| | |______| |___|   |      \    /    
  /         |          |   |   |     _ `--'      
  [   ,--.  |          |,--|   |]   (_) 
  |__/    \_|__________/    \__|= o 
     \    /            \    /
      `--'              `--' 
'''

doll = r'''
       &&&&&&&
      &&(+.+)&&
      ___\=/___
     (|_ ~~~ _|)
        )___(
      /'     `\
     ~~~~~~~~~~~
     `~//~~~\\~'
      /_)   (_\
'''

diamond = r'''

                        '
               '                 '
       '         '      '      '        '
          '        \    '    /       '
              ' .   .-"```"-.  . '
                    \`-._.-`/
         - -  =      \\ | //      =  -  -
                    ' \\|// '
      jgs     . '      \|/     ' .
           .         '  `  '         .
        .          /    .    \           .
                 .      .      .
'''

game_images = [car, doll, diamond]

nombre = input("Hola!, ¿Cual es tu nombre? \n")
print(f"Genial, {nombre}, jugaras este juego llamado ´carro, persona, diamante!´\n")
print(" Te explicare las reglas :\n \n 1) Carro aplasta Persona, pero es destruido por Diamante.\n 2) Persona destruye Diamante, pero es aplastada por Carro.\n 3) Diamante destruye Carro, pero es destruido por Persona.\n")

yo = int(input("¿Cual eliges? Escribe 0 para carro, 1 para persona y 2 para diamante. \n"))
if yo >= 0 and yo <= 2:
    print(game_images[yo])

computer = random.randint(0,2)
print("La computadora elijio: ")
print(game_images[computer])
#La razón por la que la computadora "respeta" el orden de las imágenes es que
# la lista game_images está indexada de manera secuencial (0 para carro, 1 para muñeca, 2 para diamante),
# y la computadora selecciona un número aleatorio entre 0 y 2, que luego se utiliza para acceder al índice correcto en esa lista.
#Esto mantiene el orden y asegura que tanto el jugador como la computadora vean la imagen correspondiente a su elección.

if yo >= 3 or computer < 0:  # Si yo tipeo de 3 a mas o la computadora crea un N menor a 0
    print("Tipeaste un número inválido, Perdiste :(")
elif yo == 2 and computer == 0:
    print("Ganaste !") #diamante destruye carro ESPECIFICO
elif computer == 2 and yo == 0:
    print("Sigue intentando para la proxima") # computer gana ESPECIFICO
elif yo < computer:
    print("Ganaste !") # GENERAL 0>1 Y 1>2 gana
elif computer < yo:
    print("Sigue intentando para la proxima.") #GENERAL 1<0 Y 2<1 pierde
elif yo == computer:
    print("Es un empate!")
