# services/notification_service.py

from models.notification import Notification
from services.base import dm
from datetime import datetime

class NotificationService:
    @staticmethod
    def notify(recipient_id: int, message: str) -> int:
        now = datetime.now().isoformat()
        notif = Notification(id=None, recipient_id=recipient_id,
                             message=message, created_at=now, read=False)
        return dm.add_notification(notif)
    @staticmethod
    def list_for_user(user_id: int) -> list:
        # filter dm.list_notifications() by recipient_id
        notifications = dm.list_notifications()
        user_notifications = [n for n in notifications if n.recipient_id == user_id]
        return user_notifications

    @staticmethod
    def mark_read(notification_id: int) -> None:
        # fetch then set .read = True
        notification = dm.get_notification(notification_id)
        if notification:
            notification.read = True
            dm.update_notification(notification)
        else:
            raise ValueError("Notification not found")

