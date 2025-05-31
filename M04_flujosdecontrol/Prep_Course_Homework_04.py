#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num=2
if num>0:
  print("Es amyor")
else:
  print("Es menor")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

v1=23
v2="juan"

if (type(v1)==type(v2):
  print("Son el mismo tipo de dato")
else:
  print("Son distintos tipos de datos")






# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

i=1
while i<=20:
    if i%2==0:
        print(i , "ES PAR")
    else:
        print(i , "ES IMPAR")
    i+=1
    





# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

numeros=(0,5)
for i in numeros:
    print(i^3)



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

ciclos=10
for i in range(ciclos):
  print(i



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

numero = 84 

if isinstance(numero, int) and numero > 0:
    divisor = 2
    print(f"Factores primos de {numero}:")
    
    while numero > 1:
        if numero % divisor == 0:
            print(divisor)
            
        else:
            divisor += 1
else:
    print("La variable debe contener un número entero mayor a 0.")



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
numeros=[1,2,3,4,5]
while True:
  for i in numeros:
    print(i)
  





# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
for i in  range(10):
  while True:
    print(i+1)




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

numero = 2 

while numero <= 30:
    es_primo = True
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo and numero > 1:
        print(numero)
    numero += 1


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:


numero = 2

while numero <= 30:
    if numero < 2:
        numero += 1
        continue 
    
    es_primo = True
    divisor = 2
    
    while divisor < numero:
        if numero % divisor == 0:
            es_primo = False
            break 
        divisor += 1
    
    if es_primo:
        print(numero)
    
    numero += 1


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]: mediante la toma de tiempo del proceso




# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

i = 100
while i <= 300:
    if i % 12 != 0:   
        i += 1
        continue
    print(i)
    i += 1




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

while True:
    
    if numero < 2:
        es_primo = False
    else:
        es_primo = True
        divisor = 2
        while divisor * divisor <= numero:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor += 1

  
    if es_primo:
        print(numero , " es un número primo.")
    else:
        print(numero  , " no es un número primo.")

    respuesta = input("¿Querés buscar el siguiente número primo? (s/n): ").lower()
    if respuesta != 's':
        print("¡Gracias por usar el programa!")
        break

   
    numero += 1
  
    while True:
        if numero < 2:
            es_primo = False
        else:
            es_primo = True
            divisor = 2
            while divisor * divisor <= numero:
                if numero % divisor == 0:
                    es_primo = False
                    break
                divisor += 1
        if es_primo:
            break
        numero += 1


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

i=100
while i<=300:
  if i%3==0 and i%6==0:
    print(i)
    break
  i+=1


