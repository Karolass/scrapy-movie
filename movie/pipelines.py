# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os

def createCSVIfNotExist():
  try:
    os.stat('movie.csv')
  except:
    with open('movie.csv', 'w') as file:
      writer = csv.writer(file)
      writer.writerows([['電影名稱', '片長', '上映日期', '導演', '影片年份']])

class MoviePipeline(object):
  def process_item(self, item, spider):
    createCSVIfNotExist()
    # 避免有些資料缺失
    for field in item.fields:
      item.setdefault(field, '')

    with open('movie.csv', 'a') as file:
      writer = csv.writer(file)
      writer.writerows([[item['title'], item['runtime'], item['release'], item['director'], item['year']]])

