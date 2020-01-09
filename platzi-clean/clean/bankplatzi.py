import sys

# Variable global de cliente que hara un deposito
customer_deposit = []
clients = ''


def create_clients():
    global customer_deposit

    message = 'Ingresar la cantidad de persona que desea'
    print(message)
    print('-' * len(message))

    salir = False

    while not salir:
        client_name = input('Enter your name: ')
        if client_name in customer_deposit:
            print('Cliente ya en existencia')
            break
        customer_deposit.append(client_name)
        salir = client_name == 'no'
    return customer_deposit


def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name

    else:
        print('Client already in client\'s list')


def list_clients():
    print(clients)


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _print_welcome():
    message = 'WELCOME TO BAN-PLATZI'
    print(message)
    print('-' * len(message))
    print('What would you like to do today?:')
    print('[A] Add customer to deposit row ')
    print('[AC] Add customer to account opening row ')
    print('[ATC] Attend customer ')
    print('[L] List customers in a row ')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'A':
        client_name = create_clients()
        print(client_name)
    elif command == 'AC':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'ATC':
        pass
    elif command == 'L':
        pass
