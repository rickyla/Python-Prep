#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
numero=12
print(numero)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

n2=8.5
print(n2)



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(numero))



# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre="ricardo"
print(nombre)


# 5) Crear una variable que contenga un número complejo

# In[3]:


z1=4j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(z1))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


pi_redondeado = round(pi, 4)
print(pi_redondeado)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]

v1="true"
v2=True
#son distintas porque una es string y otra booleana




# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(v1))
print(type(v2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

num=22
resultado=num+12+3.44



# 11) Realizar una operación de suma de números complejos

# In[2]:

c1=4j
c2=5j
suma=c1+c2



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

n1=2
z1=9j
suma=n1+z1



# 13) Realizar una operación de multiplicación

# In[5]:


print(2*3)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2^8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

r1=27/4
print(r1)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

r1=int(r1)
print(r1)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
resto=27%4
print(resto)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

print((4*r12)+resto)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

nombre="juan"

apellido="perez"

print(nombre + " " + apellido)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]: son distintos porque uno es string y el otro integer

print(type("2"))
print(type(2))



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
v1=2
v2="2"
v2=int(v2)




# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]: porque el decimal está expresado con coma y no con punto





# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
num=3
num-=1
print(num)





# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]: es un sistema de numeración basado en los digitos 1 y 0
print(1<<2)




# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]: porque son dos tipos distintos de datos, si los dos son integer el resultado sera 4 y si los dos son string será "22"






# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

nombre="juan"
edad=21
print("tu nombre es" + nombre + " y tu edad es" + str(edad))



