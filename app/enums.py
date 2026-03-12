from enum import Enum

class EmailCategory(str, Enum):
    WORK = "work"
    PERSONAL = "personal"
    PROMOTIONAL = "promotional"
    SPAM = "spam"

class EmailPriority(str, Enum):
    HIGH = "high"
    NORMAL = "normal"
    LOW = "low"
