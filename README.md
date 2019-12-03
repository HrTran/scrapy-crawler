# scrapy-crawler
Warning: This project is 2 years old, its parser's logic need to be updated

# Install scrapy via virtualenv

```sh
virtualenv venv -p python3
source venv/bin/activate

pip install -r requirements.txt
```

# Run Scrapy Crawler

```sh
# List spiders
scrapy list

# Crawl baomoi and store items into file
scrapy crawl baomoi -o items.json
```


```sh
# For development: Limit page crawled
scrapy crawl baomoi -s CLOSESPIDER_PAGECOUNT=1

scrapy crawl baomoi -s CLOSESPIDER_PAGECOUNT=1 -o items.json
```
