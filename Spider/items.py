# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class HotvideoItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 简介
    info = scrapy.Field()
    # 时长（秒）
    duration = scrapy.Field()
    # 封面
    cover = scrapy.Field()
    # up主
    author = scrapy.Field()
    # 播放量
    playcount = scrapy.Field()
    # 弹幕量
    danmaku = scrapy.Field()
    # 点赞
    likes = scrapy.Field()
    # 收藏
    favorite = scrapy.Field()
    # 分享
    share = scrapy.Field()
    # 评论数
    commentcount = scrapy.Field()
    # 上传地点
    publocation = scrapy.Field()
    # 上传时间
    pubtime = scrapy.Field()
    # 类型
    typename = scrapy.Field()
    # 来源
    laiyuan = scrapy.Field()
    # 投币
    coin = scrapy.Field()

