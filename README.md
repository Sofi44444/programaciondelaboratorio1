suma=0
contrasuma=0
multiplicacion=1
contramultiplicacion=1
print('Esta es la suma y multiplicacion de la matris diagonal :) ')
M=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
filas=len(M)
for i in range(4):
    for j in range(4):
        if(i==j):
            suma=suma+M[i][j]
            multiplicacion=multiplicacion*M[i][j]
            
print('Esta es la suma y multiplicacion de la contra diagonal :) ')
for i in range(4):
    for j in range(4):
        if(j==filas-1-i):
            contrasuma=contrasuma+M[i][j]
            contramultiplicacion=contramultiplicacion*M[i][j]
            
print('la suma de la diagonal es: ' + str(suma))
print('la multiplicacion de la diagonal es: '+ str(multiplicacion))
print('la suma de la contradiagonal es: '+ str(contrasuma))
print('la multiplicacion de la contradiagonal es: '+ str(contramultiplicacion))
        
print('final del ejercisio')
