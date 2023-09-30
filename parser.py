"""
Parse and validate url strings from the text file
"""
import os
import re
from urllib.parse import urlparse

from url import Url, UrlStatus
from utils import logger


class Parser:
    """
    Parse a url string list into a list of Url entities
    """

    @staticmethod
    def parse(url_file_path):
        """
        The main method for parsing a url text file
        """
        url_list = []

        try:
            with open(url_file_path, 'r') as file:
                url_str_list = file.read().split()
        except FileNotFoundError:
            logger.exception("Exception occurred when opening url list file")
            return url_list

        for url_str in url_str_list:
            try:
                parsed_url = urlparse(url_str)
            except ValueError:
                logger.execption(f"Exception occurred when parsing {url_str}")

            if parsed_url and Parser.is_valid_url(parsed_url):
                url = Url(url_str=url_str,
                          file_name=os.path.basename(parsed_url.path))
            else:
                url = Url(url_str, status=UrlStatus.INVALID)

            url_list.append(url)

        return url_list

    @staticmethod
    def is_valid_url(parsed_url):
        fqdn_pattern = r'^([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,}$'
        if re.match(fqdn_pattern, parsed_url.netloc):
            return True
        return False
