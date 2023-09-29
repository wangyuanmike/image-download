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
    DOWNLOADING = auto()
    FAILED = auto()   # download failed -> can be retried later
    ABORTED = auto()  # exceed max_retries -> abort download


class Url:
    """
    The initialization of Url object is done through the Parser
    """
    def __init__(self, url_str, status=UrlStatus.TODO, retries=0):
        self.url_str = url_str
        self.status = status
        self.retries = retries
