import unittest
from unittest.mock import patch
from .outfile_extractor import OutFileExtractor


class TestOutFileExtractor(unittest.TestCase):
    @patch("hyperworks_tools.post.datastructure.outfile.OutFile._read_lines", autospec=True)
    @patch("hyperworks_tools.post.outfile_extractor.os.walk", autospec=True)
    def test_get_out_files(self, mock_walk_files, mock_basename):
        mock_basename.return_value = []
        mock_walk_files.return_value = [(("/"), (), ("test.out", "test2.out", "test.txt"))]
        extractor = OutFileExtractor("dummy_path")
        number_out_files = len(extractor.out_files)
        self.assertEqual(number_out_files, 2)
