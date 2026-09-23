# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido: Manuel Nicolao
# Curso:2do 2da
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================

# Crear las variables necesarias.
# Crear las listas de productos y precios.
# Pedir los datos del cliente.

#usuario
nombreclient = input("Nombre: ")
dinero = int(input("¿Cual es su saldo?"))
#kiosco
productos = ["", "Agua", "Alfajor", "Tostado"]
precios = [0, 700, 900, 2200]
#cantidades
cantalf = 0
cantaguas = 0
canttost = 0
canttotal = cantalf + canttost + cantaguas
dinerogastado = cantalf * 900 + canttost * 2200 + cantaguas * 700


print("===== KIOSCO ESCOLAR =====")
print("Nombre: ", nombreclient)
print("Dinero disponible:", dinero)
print("")
print(f"Hola {nombreclient}.")
print("Saldo disponible: $", dinero)
print("")
# =========================
# ETAPA 2 - COMPRAS
# =========================

# Mostrar el menú y procesar la opción seleccionada.
# Utilizar las listas para obtener producto y precio.
print("Eliga una opcion")
print("Agua, Alfajor, Tostado")
opc = int(input("Eliga: "))
print("")

while opc > 3:
    print("opcion incorrecta")
    print("Eliga una opcion")
    print("Agua, Alfajor, Tostado")
    opc = int(input("Eliga: "))
    print("")
    
print("producto: ", productos[opc])
print("Precio:", precios[opc])

while dinero < precios[opc]:
    print("saldo insuficiente")
    print("")
    print("Eliga una opcion")
    print("Agua, Alfajor, Tostado")
    opc = int(input("Eliga: "))
    print("")
print("Compra realizada correctamente.")    
print("Saldo restante", dinero - int(precios[opc]))
if opc == 1:
    cantaguas = cantaguas + 1
if opc == 2:
    cantalf = cantalf + 1
elif opc == 3:
    canttost = canttost + 1

# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.
