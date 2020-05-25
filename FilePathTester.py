import os


class FilePathTester:
    def __init__(self):
        self.paths = []
        self.incorrectPaths = []

    def addPath(self, path):
        path = path.strip()
        if path == '':
            raise ValueError('Пустая строка!')
        if os.path.exists(path):
            self.paths.append(path)
        else:
            self.incorrectPaths.append(path)
        return True if os.path.exists(path) else False

    def removeCorrectPath(self, path):
        try:
            self.paths.remove(path.strip())
        except ValueError as error:
            return False

    def removeIncorrectPath(self, incorrectPath):
        try:
            self.incorrectPaths.remove(incorrectPath.strip())
        except ValueError as error:
            return False

    def takeIncorrectPath(self, incorrectPath):
        incorrectPath = incorrectPath.strip()
        if incorrectPath == '':
            raise ValueError('Вы не выбрали строку для повторной проверки!')
        try:
            self.incorrectPaths.remove(incorrectPath)
            return incorrectPath
        except ValueError as error:
            return False

    def moveCorrectPathToIncorrect(self, path):
        path = path.strip()
        try:
            self.paths.remove(path)
            self.incorrectPaths.append(path)
        except ValueError as error:
            return False
