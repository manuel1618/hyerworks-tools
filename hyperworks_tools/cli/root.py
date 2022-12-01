import typer
from .post_cmds import objectives_cmd

app = typer.Typer(no_args_is_help=True)
app.add_typer(objectives_cmd)
