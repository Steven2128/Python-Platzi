from collections import deque

# Variable global de cliente que hara un deposito
amount_deposit = 0
amount_account = 0
client_deposit_row = deque([])
client_account_row = deque([])


def add_client_deposit_row(client):
    
    client_deposit_row.append(client)
    print("""
    Cliente agregado a la fila de deposito correctamente!
    
    """)


def add_client_account_row(client):
    
    client_account_row.append(client)
    print("""
    Cliente agregado a la fila de apertura de cuenta correctamente!
    """)


def list_clients():
    print("""
    Fila de deposito = """+str(len(client_deposit_row))+
    """
    Fila de apertura de cuenta = """+str(len(client_account_row)))


def attend_client():
    if client_account_row:
        client_account_row.popleft()
        print("""
        Cliente de fila de cuenta atendido!
        """)
    elif not client_account_row and client_deposit_row:
        client_deposit_row.popleft()
        print("""
        Cliente de deposito atendido!
        """)
    else:
        print("""
    No hay clientes que atender!
        """)
        

def _print_welcome():
    message = '''
    WELCOME TO BANK-PLATZI'''
    print(message)
    print('-' * len(message))
    print('''
    What would you like to do today?:
    [A] Add client to deposit row 
    [AC] Add client to account opening row
    [ATC] Attend client
    [L] List clients in a row
    [E] Exit 
    
    ''')


if __name__ == '__main__':
    
    while True:
        _print_welcome()

        command = input().upper()

        if command == 'A':
            amount_deposit+=1
            add_client_deposit_row(amount_deposit)
        elif command == 'AC':
            amount_account+=1
            add_client_account_row(amount_account)
        elif command == 'ATC':
            attend_client()
        elif command == 'L':
            list_clients()
        elif command == 'S':
            print("""
            Bye! ;)
            """)
            break   
