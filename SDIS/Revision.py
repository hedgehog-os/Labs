from datetime import datetime

class Revision:

    def __init__(self, revision_number: int = 1,
                 version_hash: str = None,
                 change_history: str = None,
                 editors_notes: str = None,
                 restore_status: str = None,
                 restore_date: datetime = None
                 ):
        
        self.revsion_number = revision_number
        self.version_hash = version_hash
        self.change_history = change_history  
        self.editors_notes = editors_notes
        self.restore_status = restore_status
        self.restore_date = restore_date

    def mark_restored(self):
        """Отметить версию как восстановленную"""
        self.restore_status = "restored"
        self.restore_date = datetime.now()

    def is_restored(self):
        """Проверить, была ли версия восстановлена"""
        return self.restore_status == "restored"

    def display_summary(self):
        """Вывести краткое описание версии"""
        return (
            f"Версия #{self.revision_number}\n"
            f"Хэш: {self.version_hash}\n"
            f"Изменения: {self.change_history}\n"
            f"Заметки редактора: {self.editor_notes}\n"
            f"Статус восстановления: {self.restore_status}\n"
            f"Дата восстановления: {self.restore_date if self.restore_date else '—'}"
        )