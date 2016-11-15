# scrapy-tutorial

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

# Crawl dmoz and store items into file
scrapy crawl dmoz -o items.json
```


```sh
# For development: Limit page crawled
scrapy crawl dmoz -s CLOSESPIDER_PAGECOUNT=1

scrapy crawl dmoz -s CLOSESPIDER_PAGECOUNT=1 -o items.json
```
