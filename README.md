# image-download
A CLI for batch downloading images

## Pre-requisite
- python3
- pip install -r requirements.txt

## How to use it?
- python cli.py --help
- An example url list file `url_list.txt` can be used for testing

## General introduction
- This CLI uses a thread pool to download images in batch
- Core components include:
  - CLI
  - Orchestrator
  - Parser
  - Downloader
  - AppConfig
- These components are delibrately seperated into several classes and files to demostrate the architecture of the application and to facilitate further extension.
- For each execution, it will also generate a log file and a summary file
- Authentication, post-processing, progress visualization, and further advanced features are not implemented due to time constraints
- Also due to time constraints, only naive retry is implemented for error handling
