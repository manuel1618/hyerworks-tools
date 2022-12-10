import os
from typing import List
import typer
from .datastructure.outfile import OutFile


class OutFileExtractor:
    """
    Class to extract the objective function values from a folder containing .out files
    """

    def __init__(self, path: str) -> None:
        """
        Extracts the OutFiles from the given path and prints the objective results
        Args:
            path (str): Path to the folder containing the .out files
        """
        self.out_files = self.get_out_files(path)

    def print_objectives(self) -> None:
        """
        Prints the objective function values of the OutFiles
        """
        for out_file in self.out_files:
            typer.echo(
                f"File: {out_file.name} has reached an objective of {out_file.get_objective()}"
            )

    def get_out_files(self, path) -> List[OutFile]:
        """
        Returns a list of OutFiles from the given path
        Args:
            path (str): Path to the folder containing the .out files
        Returns:
            List[OutFile]: List of OutFiles
        """
        out_files = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".out"):
                    out_files.append(OutFile(os.path.join(root, file)))
        return out_files
