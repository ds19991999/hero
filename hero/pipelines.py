# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy

from hero.output import plus_print

# class HeroPipeline:
#     def process_item(self, item, spider):
#         return item


class HeroPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        skin_url = item['skin_url']
        yield scrapy.Request(url=skin_url, meta={'item':item})

    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        skin_name = item["skin_name"]
        hero_name = item["hero_name"]
        path = u"{}/{}".format(hero_name, skin_name+".jpg")
        return path

