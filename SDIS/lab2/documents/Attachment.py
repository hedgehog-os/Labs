import os
import hashlib

class Attachment:

    formats = {
        'pdf', 'docx', 'txt', 'md','html',
        'xlsx', 'csv', 'json', 'xml',
        'latex', 'py', 'cpp'
    }

    def __init__(self, file_size: int,
                 file_path: str,
                 format: str = None,
                 checksum: str = None,
                 linked_documents: list[str] = None,
                 ):
        self.file_size = file_size
        self.file_path = file_path
        self.format = format
        self.checksum = checksum
        self.linked_documents = linked_documents

    @property
    def format(self):
        return self._format

    @format.setter
    def format(self, value):
        if value not in self.formats:
            raise ValueError(f'Недопустимый формат: {value}')
        self.format = value

    def get_file_size(self):
        """Возвращает размер файла в байтах"""
        try:
            return os.path.getsize(self.file_path)
        except FileNotFoundError:
            return None
        
    def calculate_checksum(self):
        """Вычисляет SHA-256 хэш файла"""
        sha256 = hashlib.sha256()
        try:
            with open(self.file_path, "rb") as f:
                while chunk := f.read(8192):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except FileNotFoundError:
            return None
        
    def verify_checksum(self):
        """Проверяет, совпадает ли текущий хэш с сохранённым"""
        current_checksum = self.calculate_checksum()
        if current_checksum is None:
            print("Файл не найден.")
            return False
        if current_checksum == self.checksum:
            print("Файл не изменён. Контрольная сумма совпадает.")
            return True
        else:
            print("Файл был изменён! Контрольная сумма не совпадает.")
            return False