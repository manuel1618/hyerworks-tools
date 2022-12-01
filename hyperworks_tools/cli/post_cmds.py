import typer
from ..post.outfile_extractor import OutFileExtractor

objectives_cmd = typer.Typer(name="objectives", invoke_without_command=True)


@objectives_cmd.callback()
def objectives(
    path: str = typer.Argument(..., help="Path to the folder containing the .out files")
):
    """
    Extracts the OutFiles from the given path and prints the objective results
    """
    typer.echo(f"Path: {path}")
    OutFileExtractor(path)
