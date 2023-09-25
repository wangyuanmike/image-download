# Brainstorming

## Assumption
- URL list file should not be too big to be loaded into memory

## Configuration
- maintain authentication method for each website
- input
- output

## Batch download process
- Pre-processor
  - Load all URLs as a hashmap
  - key: url, value: status (invalid, downloaded, )
- Selector (scheduler)
  - select image URL for downloading
- Validater
  - validate URL
  - validate authentication method is maintained
- Downloader
  - Authentication
  - Send image download request (async?)
  - Error handling
  - Rate limit for the same website
  - Get image file name from URL (guess name?)
  - Save image file
- Monitor
  - Update progress
  - Persist progress
- Visualizer
  - Show progress bar (optional)

## Test website
- NASA image gallery

## Question
- Multiple input files?
- Schedule CLI as background job?
- Disk full?
- Platform difference? Mac? Windows?
- Post-processing after download?
