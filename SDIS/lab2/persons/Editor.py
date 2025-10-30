from datetime import datetime
from typing import List
class Editor:
    def __init__(self,
                 editor_id: int,
                 fullname: str,
                 email: str,
                 editor_notes: str,
                 revision_number: int,
                 change_history: str) -> None:
        self.editor_id: int = editor_id
        self.fullname: str = fullname
        self.email: str = email
        self.editor_notes: str = editor_notes
        self.revision_number: int = revision_number
        self.change_history: str = change_history

    def update_email(self, new_email: str) -> None:
        """Обновляет адрес электронной почты редактора."""
        if new_email and "@" in new_email:
            self.email = new_email

    def append_note(self, note: str) -> None:
        """Добавляет дополнительную заметку редактора."""
        if note:
            self.editor_notes += f"\n• {note}"

    def increment_revision(self) -> None:
        """Увеличивает номер ревизии на единицу."""
        self.revision_number += 1

    def record_change(self, change: str) -> None:
        """Добавляет запись об изменении в историю правок."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.change_history += f"\n[{timestamp}] {change}"

    def has_changes(self) -> bool:
        """Проверяет, есть ли записи в истории изменений."""
        return bool(self.change_history.strip())

    def get_change_log(self) -> List[str]:
        """Возвращает список всех записей истории изменений."""
        return [line for line in self.change_history.strip().split("\n") if line]

    def summarize(self) -> str:
        """Форматирует краткую информацию о редакторе."""
        return (
            f"Редактор #{self.editor_id}: {self.fullname}\n"
            f"Email: {self.email}\n"
            f"Ревизия: {self.revision_number}\n"
            f"Заметки: {self.editor_notes or '—'}\n"
            f"Изменений: {len(self.get_change_log())}"
        )

    def to_dict(self) -> dict:
        """Сериализует редактора в словарь."""
        return {
            "editor_id": self.editor_id,
            "fullname": self.fullname,
            "email": self.email,
            "editor_notes": self.editor_notes,
            "revision_number": self.revision_number,
            "change_history": self.get_change_log()
        }
