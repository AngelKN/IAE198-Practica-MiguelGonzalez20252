print("hola mundo")

nombre =  "Miguel"
edad = 22
usuario = input("Digite su nombre ")
print("hola: ",usuario)

a,b=10,3
print(a+b,a/b,a*b,a%b)
print(a>b,a==10,b!=5)

""""Hola %s" % "miguel"
"Tengo %b años" % 35
"pi = %f" % 3.14
"pi = %2f" % 3.14
nombre = "miguel"
edad = 35
print ("hola me llamo %s y tengo %b" % (nombre, edad))"""


x = 0
if x > 0:
    print("positivo")
elif x==0:
    print("es 0")
else:
    print("negativo")

#while 
i=1
while i<5:
    print(i)
    i+=1

#for
    for j in range(5):
        print(j)

#listas
numeros = [0,1,2,3]
print (numeros[0])
numeros.remove(3)
print(len(numeros))
datos = ['txt', 30, True]
numeros[1] = 5

#diccionarios
estudiante = {
    'nombre' : 'miguel',
    'edad' : 22,
    'carrera' : 'ing'
}

print(estudiante['nombre'])
estudiante['edad']=30
estudiante['nota']=8.5
print(estudiante['nombre'],estudiante['edad'],estudiante['nota'],estudiante['carrera'])

#funciones
def multiplicar(primero, segundo):
    return primero * segundo

print(multiplicar(3,2))