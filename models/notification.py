# models/notification.py

class Notification:
    def __init__(self, id=None, recipient_id=None, message="", 
                 created_at=None, read=False):
        self.id = id
        self.recipient_id = recipient_id
        self.message = message
        self.created_at = created_at
        self.read = read
