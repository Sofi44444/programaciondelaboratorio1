import random
secreto=random.randint(1,20)
intentosrealizados=0
intentosmax=6
     while(intentosrealizados<intentosmax):
         intentosrealizados=intentosrealizados+1
         print('por favor, ingrese un numero')
         x=int  (input('-->'))
         if(x<secreto):
             print('el numero es menor al numero secreto')
             else:
                 if(x>secreto):
                     print('el numero es mayor al numero secreto')
                     else:
                         if(x==secreto):
                             break
                            print('¡felicidades!, ¡gano!')
