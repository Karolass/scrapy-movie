# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.http import Request

from movie.items import MovieItem

import re

class MovieSpider(scrapy.Spider):
  name = 'movie'

  baseURL = 'http://search.atmovies.com.tw/'
  searchName = ''

  def __init__(self, *args, **kwargs): 
    super(MovieSpider, self).__init__(*args, **kwargs) 
    
    self.searchName = kwargs.get('name')

  def start_requests(self):
    searchURL = self.baseURL + 'search/'
    yield FormRequest(
      url=searchURL,
      callback=self.parseSearch,
      headers={ 'Referer': 'http://search.atmovies.com.tw/search/' },
      formdata={ 'type': 'all', 'search_term': self.searchName }
    )

  def parseSearch(self, response):
    movies = response.xpath('//div[@class="content content-left"]/blockquote/header')
    for movie in movies:
      movieType = movie.xpath('font/text()').extract()[0]
      if movieType == '電影':
        item = MovieItem()
        movieTitle = movie.xpath('a/text()').extract()[0]
        movieURL = movie.xpath('a/@href').extract()[0]
        item['title'] = movieTitle
        request = Request(
          url=self.baseURL + movieURL,
          callback=self.parseMovie
        )

        request.meta['item'] = item
        yield request

  def parseMovie(self, response):
    item = response.meta['item']
    runtimes = response.xpath('//ul[@class="runtime"]/li')
    for runtime in runtimes:
      rText = runtime.xpath('text()')

      if len(rText) > 0 and rText.extract()[0][:4] == '上映日期':
        item['release'] = rText.extract()[0][5:]
      elif len(rText) > 0 and rText.extract()[0][:2] == '片長':
        item['runtime'] = rText.extract()[0][3:]

    filmDatas = response.xpath('//div[@id="filmCastDataBlock"]/ul/li')
    for filmData in filmDatas:
      fText = filmData.xpath('b/text()')

      if len(fText) > 0 and fText.extract()[0][:2] == '導演':
        item['director'] = filmData.xpath('a/text()').extract()[0].strip()
      elif len(fText) > 0 and fText.extract()[0][:4] == '影片年份':
        item['year'] = filmData.xpath('text()').extract()[0].strip()

    return item
