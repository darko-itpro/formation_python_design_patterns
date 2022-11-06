import os.path

class Loader:
    def __new__(cls, filename):
        ext = os.path.splitext(filename)[-1]
        for sub in cls.__subclasses__():
            if sub.is_designed_for(ext):
                obj = object.__new__(sub)
                obj.__init__(filename)
                return obj

    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def is_designed_for(cls, ext):
        return ext in cls.extensions

class FileLoader(Loader):
    extensions = ['.csv']

    def load_episodes(self):
        print("Readong from file")

class DBLoader(Loader):
    extensions = ['.db']

    def load_episodes(self):
        print("Load from db")

if __name__ == '__main__':
    loader = Loader("new_data.csv")
    print(type(loader))
    loader = Loader("db_app.db")
    print(type(loader))