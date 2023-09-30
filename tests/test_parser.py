from parser import Parser
from urllib.parse import urlparse

import pyfakefs
import pytest
from url import UrlStatus


def test_is_invalid_url():
    url1 = "http://mars.jpl.nasa.gov/msl-raw-images/000I1_DXXX.jpg"
    url2 = "invalid-url"

    valid = Parser.is_valid_url(urlparse(url1))
    assert valid

    valid = Parser.is_valid_url(urlparse(url2))
    assert not valid

def test_parse_url_list_file(fs):
    file_path = '/tmp/file_path'
    file_content = """
        http://mars.jpl.nasa.gov/msl-raw-images/000I1_DXXX.jpg
        invalid-url
        https://https://mars.jpl.nasa.gov/msl-raw-images/000I1_DXXX.jpg
        https://alifei03.cfp.cn/creative/vcg/nowater800/new/VCG2108f52ee32.jpg
        https://alifei03.cfp.cn/creative/vcg/nowater800/new/VCG2108f52ee32.jpg
        https://tenfei01.cfp.cn/creative/vcg/nowater800/new/VCG2175e049668.jpg
    """
    fs.create_file(
        file_path=file_path,
        contents=file_content
    )

    url_list, host_index = Parser.parse(file_path)

    assert len(url_list) == 6
    for url in url_list:
        if url.url_str == "invalid-url" or url.url_str[:16] == "https://https://":
            assert url.status == UrlStatus.INVALID
        else:
            assert url.status == UrlStatus.TODO
        assert url.retries == 0

    assert len(host_index) == 3
    assert len(host_index["mars.jpl.nasa.gov"]) == 1
    assert len(host_index["alifei03.cfp.cn"]) == 2
    assert len(host_index["tenfei01.cfp.cn"]) == 1
