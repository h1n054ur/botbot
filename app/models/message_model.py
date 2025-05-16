from dataclasses import dataclass
from datetime import datetime

@dataclass
class MessageModel:
    sid: str
    from_number: str
    to_number: str
    body: str
    date_sent: datetime
    status: str
