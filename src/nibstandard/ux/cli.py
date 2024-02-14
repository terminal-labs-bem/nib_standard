import os

from .. import settings
from .. import app

import click

context_settings = {"help_option_names": ["-h", "--help"]}


def init():
    app.main()


@click.group(context_settings=context_settings)
@click.version_option(
    prog_name=settings.PROJECT_NAME.capitalize(), version=settings.VERSION
)
@click.pass_context
def cli(ctx):
    init()


@click.group(name="system")
def system_group():
    pass
    

@system_group.command("stub")
def system_stub_cmd():
    print("you called 'system stub'")


cli.add_command(system_group)
