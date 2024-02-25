#!/usr/gamma/'Python_intermediary python
# -*-coding:utf-8 -*-
"""
@File    :   movie.py
@Time    :   2024/02/23 14:54:07
@Author  :   MSN 
@Version :   1.0
@Contact :   mass.zenn.2014@gmail.com
@License :   (C)Copyright 2024-2025, MSN
@Desc    :   None
"""

import json

class Movie:
    BASE_URL = "https://caching.graphql.imdb.com/"
    def __init__(
        self,
        id,
        title,
        year,
        rating,
        genres,
        runtime,
        url=BASE_URL,
    ):
        self.__id = id
        self.__url = url + id
        self.__title = title
        self.__year = year
        self.__rating = rating
        self.__genres = genres
        self.__runtime = runtime

    @property
    def url(self):
        return self.__url

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    @property
    def genres(self):
        return self.__genres

    @property
    def rating(self):
        return self.__rating

    @property
    def runtime(self):
        return self.__runtime

    def to_dict(self):
        return {
                "title": self.title,
                "year": self.year,
                "rating": self.rating,
                "genres": self.genres,
                "runtime": self.runtime,
                "url": self.url,
            }

    def export_json(self):
        return json.dumps(self.to_dict())

