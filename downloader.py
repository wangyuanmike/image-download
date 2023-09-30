"""
Download operations include send request, extract file name, and save file
"""
import os
import time

import requests

from config import app_config
from url import UrlStatus
from utils import logger


class Downloader:
    """
    Download image from a certain url
    """
    def __init__(self, url):
        self.url = url

    def download(self):
        """
        The main method to download image from a certain url
        """
        if self.url.status == UrlStatus.INVALID:
            print(self.url)
            return

        response = self._get_response()
        if response is None:
            self.url.status = UrlStatus.FAILED
        else:
            self._extract_file_name(response)
            self._save_file(response)
            self.url.status = UrlStatus.DOWNLOADED
        print(self.url)

    def _get_response(self):
        while self.url.retries < app_config.max_retries:
            try:
                response = requests.get(self.url.url_str)
                response.raise_for_status()
                break
            except (requests.exceptions.RequestException, AttributeError):
                logger.exception(f"Exception getting response {self.url.url_str}")
                self.url.retires += 1
                time.sleep(app_config.retry_delay)

        return response

    def _extract_file_name(self, response):
        """
        Extract (guess) image file name and type through url or response
        """
        content_disposition = response.headers.get('content-disposition')
        if content_disposition:
            self.url.file_name = content_disposition.split('filename=')[1].strip('"')
        else:
            content_type = response.headers.get('content-type')
            if content_type:
                ext = content_type.split('/')[1].split(';')[0]
                root, _ = os.path.splitext(self.url.file_name)
                self.url.file_name = f"{root}.{ext}"

    def _save_file(self, response):
        save_path = os.path.join(app_config.output_directory, self.url.file_name)
        with open(save_path, "wb") as file:
            file.write(response.content)
