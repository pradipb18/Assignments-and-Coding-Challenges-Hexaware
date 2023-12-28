
from Exception.Exception import FileIOException


class FileIOHandler:
    @staticmethod
    def WriteToFile(data, file_path):
        try:

            with open(file_path, 'w') as file:
                file.write(data)
        except IOError as e:
            raise FileIOException(f"Error writing to file: {str(e)}")