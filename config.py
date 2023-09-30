import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read("config.ini")

class AppConfig:
    def __init__(self):
        self._output_directory = config.get("General", "output_directory")
        self._max_workers = config.getint("General", "max_workers")
        self._max_retries = config.getint("General", "max_retries")
        self._retry_delay = config.getint("General", "retry_delay")

    def update_config(self,
                      output_directory=None,
                      max_workers=None,
                      max_retries=None,
                      retry_delay=None):
        if output_directory:
            self._output_directory = output_directory
        if max_workers:
            self._max_workers = max_workers
        if max_retries:
            self._max_retries = max_retries
        if retry_delay:
            self._retry_delay = retry_delay

    @property
    def output_directory(self):
        return self._output_directory

    @property
    def max_workers(self):
        return self._max_workers

    @property
    def max_retries(self):
        return self._max_retries

    @property
    def retry_delay(self):
        return self._retry_delay

    def __str__(self):
        return (
            f"Output Directory: {self.output_directory}\n"
            f"Max Workers: {config.max_workers}\n"
            f"Max Retries: {config.max_retries}\n"
            f"Retry Delay: {config.retry_delay}\n"
        )


app_config = AppConfig()


if __name__ == "__main__":
    config = AppConfig()
    print(config)
    config.update_config(max_workers=100)
    print(config)
