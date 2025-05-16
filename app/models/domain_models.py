from dataclasses import dataclass
from datetime import datetime
from typing import Literal

@dataclass
class NumberRecord:
    number: str
    city: str
    state: str
    type: str
    price: float

@dataclass
class SearchSession:
    unique_count: int
    empty_streaks: int
    batches: int

@dataclass
class UsageStats:
    usage: float
    cost: float
    projection: float

@dataclass
class LogEntry:
    timestamp: datetime
    direction: Literal['inbound', 'outbound']
    status: str
    details: str
