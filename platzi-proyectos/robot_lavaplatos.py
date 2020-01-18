lavabo = True
def lavar():
    global add_plato

    try:
        plato_lavado = cantidadPlatos.pop()
    except IndexError:
        plato_lavado = 0

    return plato_lavado


def listar():
    """Listar platos en la pila"""
    print("Hay "+str(len(cantidadPlatos))+" platos en la pila")


#Variable Global
cantidadPlatos = []
def cantidad_Platos(cantidad):
    global cantidadPlatos
    cantidadPlatos = list(range(1, cantidad+1))
    print("Se han agregado los platos correctamente!")
   


#Ingreso de Cantidad de platos 
def _get_Platos():
    cantidad = int(input('Ingrese La Cantidad De Platos Que Desea Labar : '))
    if cantidad >= 1:
        return cantidad+len(cantidadPlatos)
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
            if lavabo is True:
                cantidad = _get_Platos()
                cantidad_Platos(cantidad)
            else:
                print("Lavabo roto!")

        elif command == 'L':
            cantidad = lavar()
            if cantidad != 0:
                print(f'El plato lavado es {cantidad}')
            else:
                lavabo = False
                print('La maquina hizo boom')
        elif command == 'LI':
            listar()
        elif command == 'S':
            print("""
            Bye! ;)
            """)
            break