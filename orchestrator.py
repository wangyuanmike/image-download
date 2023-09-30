"""
Orchestrating all operations that are needed for batch image downloading,
which is the entrypoint of the CLI.
"""
from concurrent.futures import ALL_COMPLETED, ThreadPoolExecutor, wait
from parser import Parser

from config import app_config
from downloader import Downloader
from url import Url


class Orchestrator:
    """
    Orchestrate batch download: parse url list -> use thread pool to download
    """
    def __init__(self):
        self.url_list = []

    def batch_download(self, url_file_path):
        self.url_list = Parser.parse(url_file_path)

        with ThreadPoolExecutor(max_workers=app_config.max_workers) as executor:
            tasks = [executor.submit(Downloader(url).download) for url in self.url_list]

        wait(tasks, return_when=ALL_COMPLETED)

        save_path = "./download_summary.txt"
        with open(save_path, "w") as file:
            for url in self.url_list:
                file.write(str(url) + "\n")

        print("==================================")
        print("Download is finished.")


if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.batch_download("url_list.txt")
