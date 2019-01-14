# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 管道：数据去重

# scrapy要将爬去spider和处理层pipeline分离开，使程序更容易扩展
# spider yield 生成的item会交给pipline处理。若爬去速度与处理速度不一致，scrapy会自动调度
# 爬去解析速度大于pipline，未处理的item会进入到队列中(item_chain)


class Scrapy2Pipeline(object):
    def process_item(self, item, spider):
        # 爬虫部分在for循环中yield item，所以process_item会重复执行
        # open(mode="a")追加模式("w"模式会覆盖之前的信息)
        with open("movie.txt", "a", encoding="UTF-8") as f:
            f.write(str(item.name) + "\n")
        return item
