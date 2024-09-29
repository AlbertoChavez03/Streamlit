import streamlit as st
import Funciones as Fn
import pandas as pd

st.text("TABLA DE FUNCIONES")
#1
st.title("Saludo")

nombre = st.text_input("Escribe tu nombre")
if  st.button("Precione"):
        st.write(Fn.saludar(nombre))
#2
st.title("Suma de dos Numeros ")
num1 = st.number_input("Dijite el primer numero: ",value=0)
num2 = st.number_input("Dijite el segundo numero: ",value=0)
if st.button("Precione_aqui"):
    st.write("La suma de los dos numeros ingresados es ",Fn.sumar(num1,num2))
#3
st.title("Area de un Triangulo")
base = st.number_input("Ingresa la base del triangulo",value=0)
altura = st.number_input("Ingresa la Altura del triangulo",value=0)
if st.button("Resultado"):
    st.write("El area del triangulo es: ",Fn.Area_triangulo(base,altura))
#4
st.title("Calcular descuento")
precio = st.number_input("Precio original",value=0)
descuento = st.number_input("Porcentaje del descuento(opcional:)",value=10)
impuesto = st.number_input("Impuesto (opcional)",value=16)
if st.button("resultado"):
    resultado = Fn.calcular_precio_final(precio,descuento,impuesto)
    st.write(f"El precio final es: {resultado:.2f}")
#5
st.title("Suma de numeros")
numeros_lista = st.text_input("Ingrese los numeros separados con comas (1,2,3 etc)")
if numeros_lista:
    lista = [int (x)for x in numeros_lista.split(",")]
    if st.button("Resultado_aqui"):
        st.write("La suma: ",Fn.sumar_lista(lista))
#6
st.title("Precio de un producto")
nombre_producto = st.text_input("Nombre del producto: ",value="producto")
cantidad = st.number_input("Cantidad (opcional):",value=0)
precio_unidad= st.number_input("Precio por unidad (opcional)",value=0)
if st.button("Precio final de un producto"):
    st.write("El precio total es: ",Fn.producto(nombre_producto,cantidad,precio_unidad))
#7
st.title("Numeros pares Impares")
numeros_pares_impares = st.text_input("Ingrese los numeros separados por comas (1,2,3 etc)")
lista_numeros = [int(x) for x in numeros_pares_impares.split(",") if x.strip()] #.strip Comodin para verificar que la lista no esta vacia
pares,impares = Fn.numeros_pares_e_impares(lista_numeros)
tabla_P = pd.DataFrame(pares)
st.write("Pares: ")
st.dataframe(tabla_P)
tabla_I = pd.DataFrame(impares)
st.write("Impares")
st.dataframe(tabla_I)
#8
st.title("Multiplicacion de Numeros")
numeros_multiplicar = st.text_input("Ingresa los numeros separados por comas (1,2,3 etc)")
if numeros_multiplicar:
    lista_numeros_multiplicar = [int (x) for x in numeros_multiplicar.split(",")]
    if st.button("Multiplicacion de numeros"):
        st.write("El resultado es: ",Fn.multiplicar_todos(*lista_numeros_multiplicar))
#9
st.title("Informacion Personal")
nombre_persona = st.text_input("Nombre: ")
edad = st.number_input("Edad: ", value=0)
direccion = st.text_input("Direccion: ")
if st.button("Actualizar información"):
    if nombre_persona and edad and direccion:
        datos = f"Información Personal:\nNombre: {nombre_persona}\nEdad: {edad}\nDireccion: {direccion}"
        st.write(datos)
    else:
            st.write("Por favor, completa todos los campos.")




#10
st.title("Calculadora Flexible")
num1_cal = st.number_input("Ingrese el primer numero: ",value=0)
num2_calc = st.number_input("Ingrese el segundo numero: ",value=0)
operacion = st.selectbox("Selecciona una oparacion ",["suma","resta","multiplicacion","divicion"])
if st.button("Toca"):
    st.write("El resultado es: ",Fn.calculadora_flexible(num1_cal,num2_calc,operacion))



