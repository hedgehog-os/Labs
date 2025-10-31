from datetime import datetime, timedelta
from typing import Optional
from persons.UserProfile import UserProfile
from documents.Document import Document

class AccessLog:

    actions = {
        'view', 'edit', 'download'
    }


    def __init__(self, user_id: int, action: str, email: str, timestamp: datetime, document_id: Optional[int] = None) -> None:
        self.user_id: int = user_id
        self.actions: str = action
        self.timestamp: datetime = timestamp
        self.document_id: Optional[int] = document_id
        self.email: str = email

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        if value not in self.actions:
            raise ValueError(f'Недопустимый статус: {value}')
        self._action = value

    def is_for_document(self, doc_id: int) -> bool:
        """Проверяет, относится ли лог к указанному документу."""
        return self.document_id == doc_id

    def is_recent(self, minutes: int = 60) -> bool:
        """Проверяет, был ли доступ в последние N минут."""
        return self.timestamp >= datetime.now() - timedelta(minutes=minutes)

    def is_action(self, action_type: str) -> bool:
        """Проверяет, соответствует ли лог указанному действию."""
        return self.action == action_type

    def summarize(self) -> str:
        """Форматирует краткую информацию о логе доступа."""
        doc_info = f"Документ #{self.document_id}" if self.document_id is not None else "Без документа"
        return (
            f"Доступ: {self.action}\n"
            f"Пользователь ID: {self.user_id}\n"
            f"{doc_info}\n"
            f"Время: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
        )

    def to_dict(self) -> dict:
        """Сериализует лог доступа в словарь."""
        return {
            "user_id": self.user_id,
            "action": self.action,
            "timestamp": self.timestamp.isoformat(),
            "document_id": self.document_id
        }

    def is_by_user(self, user_id: int) -> bool:
        """Проверяет, принадлежит ли лог указанному пользователю."""
        return self.user_id == user_id

    def matches_user_profile(self, profile: "UserProfile") -> bool:
        """Сравнивает лог с профилем пользователя по ID и email."""
        return self.user_id == profile.expert_id and self.email_matches(profile.email)

    def email_matches(self, email: str) -> bool:
        """Проверяет, совпадает ли email с предполагаемым адресом."""
        return hasattr(self, "email") and self.email == email

    def is_related_to(self, document: "Document") -> bool:
        """Проверяет, связан ли лог с указанным документом."""
        return self.document_id == document.document_id

    def generate_audit_entry(self) -> dict:
        """Создаёт запись для журнала аудита."""
        return {
            "timestamp": self.timestamp.isoformat(),
            "user_id": self.user_id,
            "action": self.action,
            "document_id": self.document_id
        }

    def format_for_notification(self) -> str:
        """Форматирует лог для уведомления."""
        doc_info = f"документ #{self.document_id}" if self.document_id else "неуказанный документ"
        return (
            f"Пользователь #{self.user_id} выполнил действие '{self.action}' "
            f"с {doc_info} в {self.timestamp.strftime('%Y-%m-%d %H:%M')}."
        )
