import unittest
from ProdactionCode.FilePathTester import FilePathTester


class TestFilePathTester(unittest.TestCase):
    def setUp(self):
        self.path = 'C:\\Program Files'
        self.incorrectPath = 'C::s'
        self.filePathTester = FilePathTester()

    def test_add_path(self):
        self.filePathTester.addPath(self.path)
        self.assertIn(self.path, self.filePathTester.paths)

    def test_add_incorrect_path(self):
        self.filePathTester.addPath(self.incorrectPath)
        self.assertIn(self.incorrectPath, self.filePathTester.incorrectPaths)

    @unittest.expectedFailure
    def test_add_empty_path(self):
        self.assertRaises(ValueError, self.filePathTester.addPath(''))

    def test_remove_path(self):
        self.filePathTester.addPath(self.path)
        self.filePathTester.removeCorrectPath(self.path)
        self.assertNotIn(self.path, self.filePathTester.paths)

    def test_remove_no_path(self):
        result = self.filePathTester.removeCorrectPath(self.path)
        self.assertEqual(result, False)

    def test_remove_incorrect_path(self):
        self.filePathTester.addPath(self.incorrectPath)
        self.filePathTester.removeIncorrectPath(self.incorrectPath)
        self.assertNotIn(self.incorrectPath, self.filePathTester.incorrectPaths)

    def test_remove_no_incorrect_path(self):
        result = self.filePathTester.removeIncorrectPath(self.incorrectPath)
        self.assertEqual(result, False)

    def test_move_path(self):
        self.filePathTester.addPath(self.path)
        self.filePathTester.moveCorrectPathToIncorrect(self.path)
        self.assertEqual(True,
                         self.path in self.filePathTester.incorrectPaths,
                         self.path not in self.filePathTester.paths)

    def test_move_no_path(self):
        result = self.filePathTester.moveCorrectPathToIncorrect(self.path)
        self.assertEqual(result, False)

    def test_take_incorrect_path(self):
        self.filePathTester.addPath(self.incorrectPath)
        incorrectPath = self.filePathTester.takeIncorrectPath(self.incorrectPath)
        self.assertEqual(True,
                         self.incorrectPath not in self.filePathTester.incorrectPaths,
                         incorrectPath == self.incorrectPath)

    @unittest.expectedFailure
    def test_take_empty(self):
        self.assertRaises(ValueError, self.filePathTester.takeIncorrectPath(''))
