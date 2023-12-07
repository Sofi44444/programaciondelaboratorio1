import random
secreto=ramdom.ranint(1,20)
intentosrealizados=0
intentosmaximos=6
secreto=ramdom.randint(1,200)
intentosrealizados=0
intentosmaximos=7
if(secreto1f and secreto2d):
    print('¿que dificultad quieres?')
    input('1f')
    input('2d')
    while(intentosrealizados<intentosmaximos):
        intentosrealizados=intentosmaximos+1
        print('por favor ingrese un numero ')
        x=int(input('-->'))
        if(x<secreto):
            print('el numero es menor al numero secreto')
        else:
            if(x>secreto):
                print('el numero es mayor al numero secreto')

            else:
                if(x==secreto):
                    break
                print('felicidades usted GANO!!!!!')

  
  