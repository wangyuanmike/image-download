"""
The url object, which is the core entity of this application
"""
from enum import Enum, auto


class UrlStatus(Enum):
    """
    Status of Url entity
    """
    TODO = auto()
    INVALID = auto()
    DOWNLOADED = auto()
    FAILED = auto()


class Url:
    """
    The initialization of Url object is done through the Parser
    """
    def __init__(self, url_str, status=UrlStatus.TODO, retries=0, file_name=""):
        self.url_str = url_str
        self.status = status
        self.retries = retries
        self.file_name = file_name

    def __str__(self):
        return f"{self.url_str}, {self.file_name}, {self.status.name}"
