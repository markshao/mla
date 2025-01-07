from dotenv import load_dotenv
load_dotenv()

import os
from database import init_database_with_schema
import click




@click.group()
def main_cli():
    pass

from commands import load_price
main_cli.add_command(load_price)

def main():
    """Main entry point for the script

    This function is the entry point for the script. It calls the
    :func:`init_database_with_schema` function to initialize the
    database with the schema.
    """
    init_database_with_schema()

    main_cli()
    
if __name__ == "__main__":
    main()
