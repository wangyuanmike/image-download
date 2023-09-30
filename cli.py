import click

from config import AppConfig, app_config
from orchestrator import Orchestrator


@click.command()
@click.argument("url_list_file", type=click.Path(exists=True), metavar="URL_LIST_FILE")
@click.argument("output_directory", type=click.Path(), metavar="OUTPUT_DIRECTORY")
@click.option("--max_workers", type=int,
              help="Maximum number of worker threads for concurrent downloads.")
@click.option("--max_retries", type=int,
              help="Maximum number of download retries on failure.")
@click.option("--retry_delay", type=int,
              help="Delay in seconds between download retries.")
def download_images(url_list_file, output_directory, max_workers, max_retries, retry_delay):
    app_config.update_config(output_directory=output_directory,
                             max_workers=max_workers,
                             max_retries=max_retries,
                             retry_delay=retry_delay)

    orchestrator = Orchestrator()
    orchestrator.batch_download(url_list_file)


if __name__ == "__main__":
    download_images()
