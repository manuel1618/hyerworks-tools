import os
from typing import List


class OutFile:
    """
    Class to read and store data from an .out file
    """

    def __init__(self, filepath) -> None:
        """
        Constructor
        :param filepath: path to the .out file
        returns: None
        """
        self.filepath = filepath
        self.name = os.path.basename(filepath)
        self.lines = self._read_lines()

    def _read_lines(self) -> List[str]:
        """
        Read the lines of the .out file
        returns: None
        """
        with open(self.filepath, "r", encoding="utf-8") as file:
            return file.read().splitlines()

    def get_objective(self) -> float:
        """
        Get the objective function value from the .out file
        return: objective function value
        """
        objective = 0.0
        for i, line in enumerate(self.lines):
            if "ITERATION" in line:
                # iterate over the next 10 lines until the line starts with "Objective"
                for j in range(10):
                    line = self.lines[i + j]
                    if line.strip().startswith("Objective Function"):
                        objective = float(line.split("=")[1].strip().split(" ")[0])
                        break
        return objective
