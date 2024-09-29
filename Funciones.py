


def saludar(nombre):
    return f"Hola,{nombre}"

def sumar(num1,num2):
    return num1 + num2

def Area_triangulo(base, altura):
    return base * altura / 2

def calcular_precio_final(precio, descuento=10,impuesto=16):
    precio_descuento = precio * (1 - descuento /100)
    precio_final = precio_descuento * (1 + impuesto / 100)
    return precio_final

def sumar_lista(numeros):
    num = sum(numeros)
    return num

def producto(nombre_producto,cantidad=1,precio_individual=10,):
    return f"{cantidad},{nombre_producto},{precio_individual*cantidad}"

def numeros_pares_e_impares(numeros):
    pares = []   
    impares = [] 
    
    for num in numeros:
        if num % 2 == 0: 
            pares.append(num)
        else:          
            impares.append(num)

    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def informacion_personal(**kwarks):
    if not kwarks:
        return "No se proporciono información"
    info = "Información Personal: \n"
    for clave, valor in kwarks.items():
        info += f"{clave.capitalize()}: {valor}\n"
    return info

def calculadora_flexible(num1, num2, operacion= "suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "divicion":
        return num1/num2 if num2 != 0 else "Error divicion por cero"
    else:
        return "Operacion no valida"




