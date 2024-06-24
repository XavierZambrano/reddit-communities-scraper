# reddit-communities-scraper
Reddit Communities Scraper

## Installation

### Setup
1. Clone the repository 
```
git clone https://github.com/XavierZambrano/reddit-communities-scraper.git
```
2. Create a virtual environment and activate it
3. Install the requirements
```bash
pip install -r requirements.txt
```

## Usage
```
scrapy crawl communities -O results.csv
```
For more information about scrapy crawl arguments, check the [Scrapy documentation](https://docs.scrapy.org/en/latest/topics/commands.html#std-command-crawl).

Example result: [results.csv](assets/results.csv) (it does not contain all the data, just a few rows for demonstration purposes)