# 🕷️ Hot Video Scrapy Crawler | 热门视频 Scrapy 爬虫

> **Full-stack web crawler for hot video data using Scrapy. Spider for video platform, data pipelines, batch generation, CSV export, and complete deployment scripts. Production-ready crawling solution.**
>
> 基于 Scrapy 的热门视频全栈爬虫。视频平台 Spider、数据管道、批量生成、CSV 导出、完整部署脚本。生产级爬虫解决方案。

---

## 🌟 Features | 核心特性

- **Scrapy Framework** — Production-grade web crawling
- **Hot Video Spider** — Crawl trending video data
- **Data Pipelines** — Clean, validate, store data
- **Batch Generation** — Generate crawl tasks in batch
- **CSV Export** — Export results to CSV format
- **Middleware** — Custom downloader middleware
- **Config Management** — INI-based configuration
- **One-Click Deploy** — Windows batch scripts for install/run

---

## 📁 Project Structure | 项目结构

```
Hot-Video-Scrapy-Crawler/
├── Spider/
│   ├── spiders/
│   │   └── HotvideoSpider.py       # Main crawler spider
│   ├── config/
│   │   └── config.ini               # Configuration file
│   ├── items.py                     # Data item definitions
│   ├── middlewares.py               # Downloader middleware
│   ├── pipelines.py                 # Data processing pipelines
│   └── settings.py                  # Scrapy settings
├── run.py                           # Run script
├── batchgen.py                      # Batch task generator
├── elr12v47_hotvideo.csv           # Sample output data
├── scrapy.cfg                       # Scrapy config
├── requirements.txt
├── .gitignore
├── 安装.bat                          # Windows install script
├── 运行.bat                          # Windows run script
├── README.md
├── 热门视频爬虫项目-技术深拆与复用指南.md
└── 博客要求
```

---

## 🚀 Quick Start | 快速开始

```bash
# Install dependencies
pip install -r requirements.txt
# or Windows: 安装.bat

# Run crawler
python run.py
# or Windows: 运行.bat

# Generate batch tasks
python batchgen.py

# Output: elr12v47_hotvideo.csv
```

---

## 🔧 Spider Configuration | 爬虫配置

### config.ini | 配置文件

```ini
[spider]
name = hotvideo
start_urls = https://example.com/videos
max_pages = 100
delay = 2

[output]
format = csv
filename = hotvideo.csv
encoding = utf-8
```

### Data Items | 数据字段

| Field | Description |
|-------|-------------|
| title | Video title |
| author | Uploader name |
| views | View count |
| likes | Like count |
| comments | Comment count |
| duration | Video duration |
| publish_time | Publish timestamp |
| url | Video URL |
| category | Video category |
| tags | Video tags |

---

## 📊 Pipeline | 数据管道

1. **Validation** — Check required fields
2. **Cleaning** — Remove HTML tags, normalize text
3. **Deduplication** — Remove duplicate entries
4. **Storage** — Save to CSV/database
5. **Export** — Generate final output file

---

## 📄 License | 许可证

MIT License.

---

<div align="center">

**Built with 🕷️ for web data collection**

[GitHub](https://github.com/Windyhhh/Hot-Video-Scrapy-Crawler)

</div>
