# Simulacion de plato
add_plato = [10, 23, 5, 9]

def agregar():
    """Agregar plato al lavabo"""
    pass


# def lavar():
#     global add_plato

#     while add_plato != 0:
#         print(add_plato)
#         cantidad = add_plato[0]
#         print(f'Se esta labando la cantidad de {cantidad}')
#         add_plato.pop(0)
#         if not add_plato:
#             print('La maquina hizo boom')
#             break
# Esta forma es mas automatica
def lavar():
    global add_plato

    plato_lavado = add_plato.pop(0)

    return plato_lavado


def listar(ctx):
    """Listar platos en la pila"""
    pass

#Lista de la cantidad de platos almacenados
def list_cantidad():
    print('La cantidad de Platos Ingresados Para Labar es : ',cantidadPlatos )
   
#Variable Global

cantidadPlatos = []

#Cantidad de Platos
def cantidad_Platos(cantidad):
    global cantidadPlatos
    
    if cantidad >= '1':
        cantidadPlatos.append(cantidad) 
    else: 
        print ('La cantidad no es permitida \n 0 o se pasa de limite')


#Ingreso de Cantidad de platos 
def _get_Platos():
    cantidad = input('Ingrese La Cantidad De Platos Que Desea Labar : ')

    if cantidad >= '1':
       
        return cantidad  
    else:
        print ('Usted esta enviando la cantidad 0 Error \n Minimo 1')
        _get_Platos() 
  



def print_welcome():
    message = '''
    BIENVENIDO A PLATZI-CLEAN'''
    print(message)
    print('-' * len(message))
    print('''
    Qué quieres hacer hoy?:
    
    [A] Agregar plato al lavabo
    [L] Lavar plato de la pila
    [LI] Listar platos en la pila
    [S] Salir 
    
    ''')


if __name__ == "__main__":
    """Maneja los comandos de limpieza del robot"""
    while True:
        print_welcome()
        command = input().upper()

        if command == 'A':
            cantidad = _get_Platos()
            cantidad_Platos(cantidad)
            list_cantidad()

        elif command == 'L':
            cantidad = lavar()
            if cantidad != 0:
                print(f'El plato lavado es {cantidad}')
            else:
                print('El robot hizo boom')
        elif command == 'LI':
            pass
        elif command == 'S':
            print("""
            Bye! ;)
            """)
            break