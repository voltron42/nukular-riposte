""" This module provides the Nukular Riposte CLI """
# nukular-riposte/cli.py

from typing import Optional

import typer

from NukularRiposte import __app_name__, __version__

from NukularRiposte.buildType import BuildType

app = typer.Typer()

def _parse_buildType(name: str) -> BuildType:
    return BuildType[name]

@app.command()
def new(
        type: BuildType = typer.Argument(callback=_parse_buildType, default=BuildType.Namespace)
) -> None:
    return

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
