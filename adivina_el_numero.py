#Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido 
#un número que no está permitido. 
# Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a 
#decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.  
# Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la 
#misma manera.  
# Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos 
#intentos le ha tomado.  


from random import randint
intentos = 0
numero_secreto = randint(1,100)
nombre = input('dime tu nombre: ')

print(f'bueno {nombre} he pensado un numero del 1 al 100 \n tienes 8 intentos')

while intentos < 8:
    estimado = int(input("cual es el numero?: "))
    intentos += 1
    if estimado not in range(1,101):
        print('tu numero no se encuentra en el rango de numeros de 1 a 100')

    if estimado < numero_secreto:
        print('mi numero es mas alto')

    if estimado > numero_secreto:
        print('mi numero es mas bajo')


    if estimado == numero_secreto:
        print(f'felicitacciones {nombre} has adivinado en {intentos} intentos') 
        break       

if estimado != numero_secreto:
    print(f'lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}')    