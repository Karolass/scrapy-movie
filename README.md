# Python scrapy movie

使用Python scrapy爬電影資訊，並儲存成csv檔。

## How to build

```bash
# 安裝 Python3
brew install python

# PS: Python3會自動安裝幫你安裝pip3
# 安裝scrapy
pip3 install scrapy
```

## How to run

```bash
# 參數 name: 電影名稱
scrapy crawl movie -a name=火影
```

## Structure of Source Code

```
.
├── movie
│   ├── spiders
│   │   ├── __init__.py
│   │   └── movie.py - 爬蟲主程式
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   └── settings.py
├── README.md
└── scrapy.cfg
```
