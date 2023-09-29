"""
Parse and validate url strings from the text file
"""
import re
from collections import defaultdict
from urllib.parse import urlparse

from url import Url, UrlStatus


class Parser:
    """
    Parse a url string list into a list of Url entities
    """

    @staticmethod
    def parse(url_file_path):
        """
        The main method for parsing a url text file
        - read url from text file
        - validate url
        - create url object
        - append url object to list and update host index hashmap
        - return url object list and host index
        """
        url_list = []
        host_index = defaultdict(list)

        try:
            with open(url_file_path, 'r') as file:
                url_str_list = file.read().split()
        except FileNotFoundError:
            # TODO: log error and return empty list
            return url_list, host_index

        for url_str in url_str_list:
            valid, host = Parser.is_valid_url(url_str)
            if valid:
                url = Url(url_str)
                host_index[host].append(url)
            else:
                url = Url(url_str, status=UrlStatus.INVALID)
            url_list.append(url)

        return url_list, host_index

    @staticmethod
    def is_valid_url(url_str):
        fqdn_pattern = r'^([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,}$'
        try:
            parsed_url = urlparse(url_str)
            if re.match(fqdn_pattern, parsed_url.netloc):
                return True, parsed_url.netloc
        except ValueError:
            pass

        return False, ''
