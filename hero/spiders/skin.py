# -*- coding: utf-8 -*-
import scrapy
from hero.output import plus_print
from hero.items import HeroItem

class SkinSpider(scrapy.Spider):
    name = 'skin'
    allowed_domains = ['pvp.qq.com', 'game.gtimg.cn']
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    def parse(self, response):
        # extract() 提取数据
        host_name = "https://pvp.qq.com/web201605/"
        hero_a_links = response.xpath('//div[@class="herolist-box"]/div[@class="herolist-content"]/ul/li/a')
        for link in hero_a_links:
            # ./ 表示当前标签
            href = link.xpath('./@href').extract()[0]
            hero_url = host_name + href
            yield scrapy.Request(hero_url, self.detail_parse, meta={"hero_url":hero_url})

        # 详细英雄页面处理
    def detail_parse(self, response):
        hero_url = response.meta['hero_url']
        message = response.xpath('/html/body/script[10]/text()').extract()[0]
        message_temp = message.strip().replace("'", "").split(",")
        hero_name = message_temp[0].split(" = ")[-1]
        hero_id = message_temp[1].split(" = ")[-1].replace(";", "")
        plus_print("开始解析英雄<{}>皮肤下载链接: {}".format(hero_name, hero_url))
        skin_name = response.xpath('//div[@class="pic-pf"]/ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname').extract()[0]
        skin_name = skin_name.split("|")
        for i in range(len(skin_name), 0, -1):
            name = skin_name[i-1][:-2].replace("&", "")
            skin_url = "https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg".format(hero_id, hero_id, i)
            item = HeroItem()
            item["skin_name"] = name
            item["hero_name"] = hero_name
            item["skin_url"] = skin_url
            yield item
            plus_print("正在下载英雄<{}>皮肤<{}>: {}".format(hero_name, name, skin_url))

