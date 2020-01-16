def agregar():
    """Agregar plato al lavabo"""
    pass


def lavar(ctx):
    """Lavar plato de la pila"""
    pass
           

def listar(ctx):
    """Listar platos en la pila"""
    pass

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
            pass
        elif command == 'L':
            pass
        elif command == 'LI':
            pass
        elif command == 'S':
            print("""
            Bye! ;)
            """)
            break