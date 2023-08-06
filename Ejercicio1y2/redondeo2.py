from redondeo import redondear
def usuario_numero(a):
    return redondear(a)
    
x= float(input("Ingrese un numero decimal:"))
print(usuario_numero(x))