import click

from clean import command as clean_commands


@click.group()
@click.pass_context
def cli(ctx):
    """Esta es una aplicación en CLI para lavar platos. Disfrutala!!"""

    
cli.add_command(clean_commands.all)
   

