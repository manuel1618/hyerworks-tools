import unittest
from unittest.mock import patch
from .outfile import OutFile


class TestOutFile(unittest.TestCase):

    outfile_content = """
    ITERATION   0

    Objective Function (Minimize WCOMP) =  2.00000E-10   % change =       -52.75

    ITERATION   1

    Objective Function (Minimize WCOMP) =  1.00000E+00   % change =       -52.75
    """

    @patch("hyperworks_tools.post.datastructure.outfile.OutFile._read_lines", autospec=True)
    @patch("hyperworks_tools.post.datastructure.outfile.os.path.basename", autospec=True)
    def test_extract_objectives(self, mock_basename, mock_read_lines):
        mock_basename.return_value = "test.out"
        mock_read_lines.return_value = self.outfile_content.splitlines()
        outfile = OutFile("test.out")
        objective_expected = 1.0
        objective_actual = outfile.get_objective()
        print(objective_actual)
        self.assertEqual(objective_actual, objective_expected)
