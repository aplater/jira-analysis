import click

from analyse import analyse as run_analyse
from update_tickets import load_from_file, persist_to_database


@click.group()
def cli():
    click.echo("Starting")


@cli.command()
def analyse():
    """Analyse the ticket data in the DB.
    """
    run_analyse()


@cli.command()
@click.argument("ticket_file", type=click.File())
def load(ticket_file):
    """Load tickets from the passed-in file.
    
    :param ticket_file: Path to the tickets to load (in XML format)
    """
    soup = load_from_file(ticket_file)
    persist_to_database(soup)


if __name__ == "__main__":
    cli()