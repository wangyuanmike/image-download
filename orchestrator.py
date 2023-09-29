"""
Orchestrating all operations that are needed for batch image downloading,
which is the entrypoint of the CLI.
"""


class Orchestrator:
    """
    Operations that need to be orchestrated:
        - Batch download: parse -> schedule(iterator) -> download -> extract -> save
        - Progress check: persist progress, show progress
    """
    def __init__(self):
        pass

    def batch_download(self):
        pass

    def monitor(self):
        pass


class Url:
    """
    Url eniity
    """
    def __init__(self, url_str):
        pass


class Parser:
    """
    Parse a url string list into a list of Url entities
    """
    def __init__(self):
        pass


    def validate(self, url_str):
        pass


    def parse(self, url_str):
        pass


    def append(self):
        pass


class Scheduler:
    """
    An iterator which decide the sequence of url download
    """
    def __init__(self, url_list):
        pass

    def next(self):
        pass

    def has_next(self):
        pass


class Downloader:
    """
    Download image from url
    """
    def __init__(self, url):
        pass

    def extract(self):
        """
        Extract (guess) image file name and type through url or response
        """
        pass

    def download(self, url):
        pass

    def save(self):
        pass


class PostProcessor:
    """
    Post-processing operations (e.g. compression, corruption check) after image download
    """
    def __init__(self):
        pass


class Monitor:
    """
    Monitor and persist the download progress
    """
    def __init__(self):
        pass

    def persist_progress(self):
        pass

    def show_progress(self):
        pass

