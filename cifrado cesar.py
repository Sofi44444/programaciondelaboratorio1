alfabeto=('a,b,c,d,e,f,g,h,i,j,k,l,m,ñ,o,p,q,r,s,t,u,v,w,y,z')

print('por favor ingrese la palabra que usted desee: ')
palabra=input('palabra: ')

cifrado=""

for letra in palabra.upper():
    if letra in alfabeto:
        indice=alfabeto.find(letra)
        indice+=palabra
        if indice>=26:
            indice<=26
        cifrado += alfabeto[indice]
    else:
         cifrado+=letra
print('Este es el final del ejercisio')
  
  