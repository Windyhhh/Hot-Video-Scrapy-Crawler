<div align="center">

# 热门视频爬虫 | Hot-Video-Scrapy-Crawler

### A Scrapy crawler for hot videos.

Spider, pipeline, batch generation and CSV export — a full-stack Scrapy solution for hot-video data.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2-60A839?logo=scrapy&logoColor=white)](https://scrapy.org/)

</div>

---

**Hot-Video-Scrapy-Crawler** is a full-stack **Scrapy** crawler for hot-video data — with a spider, pipelines, batch generation and **CSV export**.

> [!NOTE]
> 中文项目：Scrapy 热门视频爬虫——spider、pipeline、批量生成、CSV 导出，全栈方案。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Hot-Video-Scrapy-Crawler.git
cd Hot-Video-Scrapy-Crawler

pip install -r requirements.txt

# Run the crawler
python run.py

# Batch generation
python batchgen.py
```

Results export to CSV (see `elr12v47_hotvideo.csv` for an example output).

---

## Features

- **Scrapy spider** — `HotvideoSpider` with middlewares and pipelines.
- **Batch generation** — `batchgen.py` for large-scale runs.
- **CSV export** — structured hot-video records.

---

## Project Structure

```
Hot-Video-Scrapy-Crawler/
├── Spider/
│   ├── spiders/HotvideoSpider.py
│   ├── pipelines.py
│   ├── middlewares.py
│   ├── items.py, settings.py
│   └── config/config.ini
├── run.py, batchgen.py
├── scrapy.cfg
└── requirements.txt
```

---

## 技术实现细节

### 架构概览

项目采用模块化设计，核心目录包括：**Spider**。

### 关键函数

- `db_connect`, `batch`

### 技术栈与依赖

**主要 import**：
```python
import os
import configparser
import os
import random
import pymysql
import pymssql
from pymysql.cursors import DictCursor
```

### 实现要点

- 通过 `db_connect` 等函数实现核心流程编排
- 代码结构清晰，模块间低耦合，便于扩展和维护

---
## License

MIT — free to use, modify and distribute.
