import click



@click.group()
def clean():
    """Maneja los comandos de limpieza del robot"""
    pass


@clean.command()
@click.pass_context
def agregar(ctx):
    """Agregar plato al lavabo"""
    pass


@clean.command()
@click.pass_context
def lavar(ctx):
    """Lavar plato de la pila"""
    pass
        
        
@clean.command()
@click.pass_context
def listar(ctx):
    """Listar platos en la pila"""
    pass


all = clean