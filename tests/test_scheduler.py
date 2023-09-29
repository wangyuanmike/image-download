import pytest
from scheduler import FIFOScheduler
from url import Url


def test_fifo_scheduler():
    url_list = []
    url_list.append(Url("https://example.com/1.jpg"))
    url_list.append(Url("https://google.com/2.jpg"))
    url_list.append(Url("https://nasa.gov/3.jpg"))
    url_list.append(Url("https://example.com/4.jpg"))
    url_list.append(Url("https://google.com/5.jpg"))

    url_iterator = FIFOScheduler(url_list)
    for index, url in enumerate(url_iterator):
        assert url.url_str == url_list[index].url_str
