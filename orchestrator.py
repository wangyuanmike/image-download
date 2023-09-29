"""
Orchestrating all operations that are needed for batch image downloading,
which is the entrypoint of the CLI.
"""
from url import Url


class Orchestrator:
    """
    Operations that need to be orchestrated:
        - Batch download: parse -> schedule(iterator) -> download -> extract -> save
        - Progress check: persist progress, show progress
    """
    def __init__(self):
        self.url_list = []

    def batch_download(self, url_txt_path):
        self.url_list = Parser.parse(url_txt_path)

    def monitor(self):
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

