#!/usr/gamma/'Python_intermediary python
# -*-coding:utf-8 -*-
"""
@File    :   main.py
@Time    :   2024/02/22 11:37:37
@Author  :   MSN 
@Version :   1.0
@Contact :   mass.zenn.2014@gmail.com
@License :   (C)Copyright 2024-2025, MSN
@Desc    :   None
"""

import requests
import json
import time
from movie import Movie
from pathlib import Path
import os
import logging

URL = "https://caching.graphql.imdb.com/"
QTY = 400

headers = {
    "authority": "caching.graphql.imdb.com",
    "accept": "application/graphql+json, application/json",
    "accept-language": "en-US,en;q=0.9,fr;q=0.8",
    "content-type": "application/json",
    # 'cookie': 'session-id=133-1434679-5554117; session-id-time=2082787201l; ad-oo=0; ci=eyJhY3QiOiJDUDZWR0lBUDZWR0lBRjRBQkNFTmZyLWdBQUFBQUFBQUFCYWdBQVFBQUFBZ0FBQUEiLCJnY3QiOiJDUDZWR0lBUDZWR0lBRjRBQkNFTkFiRWdBQUFBQUFBQUFCYWdBQVFBQUFBZ0FBRkFvQU1BQVFmUUNRQVlBQWctZ09nQXdBQkI5QWxBQmdBQ0Q2QlNBREFBRUgwQXdBR0FBSVBvQ2dBTUFBUWZRR0FBWUFBZy1nUUFBd0FCQjlBUUFQQUJBQUNRQUZRQU5ZQXdnREVBR1lBT1lBZ0FCU2dEVkFKYUFWa0Fyd0J3Z0ZoZy5ZQUFBQUFBQUFBQSIsInB1cnBvc2VzIjpbXSwidmVuZG9ycyI6W119; ubid-main=132-5455927-3384765; uu=eyJpZCI6InV1YjIxMzFlNzkwMTQ5NGY2ZDllY2QiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=qTEEFxOOf2izvlPJuMKnORf0YwVSMRhSUojZCIOYgGu/bcE7sbboVqEf9xuXN0FNSYx87UmoUvlxoDE9uTlAqis4BP+VzdbnLhiGQg5S0xWTmVrIuhQOsJg8jkmkCT/fvboIs2bqoizpHTUfbZY/0N7nAcTdZ+gqmdXcspsa1PpdI56/VK9fo00S2L5xtSqfpM2pH53sOlBmG+pZoV06oscvVuuu3OWcci7awGzaXepz3zqZiBiMS/VJ0R9FGlLKjg6HR7UYU/OEpvyE0Qi+lQAiOsWxsR5Po5pyyhbhQBzOjBt392OO2KiVK76kD9HN8opA0EeWNb1buOlaoSr8Yw8brSkfNVMF',
    "origin": "https://www.imdb.com",
    "referer": "https://www.imdb.com/",
    "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "x-amzn-sessionid": "133-1434679-5554117",
    "x-imdb-client-name": "imdb-web-next-localized",
    "x-imdb-client-rid": "AK26M64XK2ZZGDJQS4R7",
    "x-imdb-user-country": "US",
    "x-imdb-user-language": "en-US",
    "x-imdb-weblab-treatment-overrides": '{"IMDB_DESKTOP_SEARCH_ALGORITHM_UPDATES_577300":"T1","IMDB_NAV_PRO_FLY_OUT_Q1_REFRESH_848923":"T2"}',
}

params = {
    "operationName": "AdvancedTitleSearch",
    "variables": f'{{"certificateConstraint":{{}},"colorationConstraint":{{}},"creditedCompanyConstraint":{{}},"first":{QTY},"genreConstraint":{{}},"listConstraint":{{"inAllLists":[],"inAllPredefinedLists":[],"notInAnyList":[],"notInAnyPredefinedList":[]}},"locale":"en-US","releaseDateConstraint":{{"releaseDateRange":{{}}}},"runtimeConstraint":{{"runtimeRangeMinutes":{{}}}},"sortBy":"POPULARITY","sortOrder":"ASC","titleTypeConstraint":{{"anyTitleTypeIds":["movie"]}},"userRatingsConstraint":{{"aggregateRatingRange":{{}},"ratingsCountRange":{{}}}}}}',
    "extensions": '{"persistedQuery":{"sha256Hash":"e7a1c7b10a7a9765731e5c874cef0342dfbd0dd7a87fa796e828778e54a07a20","version":1}}',
}


def get_json(url: str, params: dict, headers: dict, end_cursor=None):
    if end_cursor:
        params["variables"] = (
            f'{{"after":"{end_cursor}","certificateConstraint":{{}},"colorationConstraint":{{}},"creditedCompanyConstraint":{{}},"first":{QTY},"genreConstraint":{{}},"listConstraint":{{"inAllLists":[],"inAllPredefinedLists":[],"notInAnyList":[],"notInAnyPredefinedList":[]}},"locale":"en-US","releaseDateConstraint":{{"releaseDateRange":{{}}}},"runtimeConstraint":{{"runtimeRangeMinutes":{{}}}},"sortBy":"POPULARITY","sortOrder":"ASC","titleTypeConstraint":{{"anyTitleTypeIds":["movie"]}},"userRatingsConstraint":{{"aggregateRatingRange":{{}},"ratingsCountRange":{{}}}}}}'
        )
    else:
        params["variables"] = (
            f'{{"certificateConstraint":{{}},"colorationConstraint":{{}},"creditedCompanyConstraint":{{}},"first":{QTY},"genreConstraint":{{}},"listConstraint":{{"inAllLists":[],"inAllPredefinedLists":[],"notInAnyList":[],"notInAnyPredefinedList":[]}},"locale":"en-US","releaseDateConstraint":{{"releaseDateRange":{{}}}},"runtimeConstraint":{{"runtimeRangeMinutes":{{}}}},"sortBy":"POPULARITY","sortOrder":"ASC","titleTypeConstraint":{{"anyTitleTypeIds":["movie"]}},"userRatingsConstraint":{{"aggregateRatingRange":{{}},"ratingsCountRange":{{}}}}}}'
        )
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        try:
            return (
                response.json(),
                response.json()["data"]["advancedTitleSearch"]["pageInfo"]["endCursor"],
            )
        except Exception as e:
            raise e(f"Error decoding JSON: {e}\nResponse content:{response.content}")
    else:
        raise Exception(
            f"Request failed with status code: {response.status_code}\nResponse content:{response.content}"
        )


def extract_movies(json_data):
    for edge in json_data["data"]["advancedTitleSearch"]["edges"]:
        yield Movie(
            id=(
                edge["node"]["title"]["id"]
                if edge["node"]["title"]["id"] is not None
                else None
            ),
            title=(
                edge["node"]["title"]["titleText"]["text"]
                if edge["node"]["title"]["titleText"] is not None
                else None
            ),
            year=(
                edge["node"]["title"]["releaseYear"]["year"]
                if edge["node"]["title"]["releaseYear"] is not None
                else None
            ),
            rating=(
                edge["node"]["title"]["ratingsSummary"]["aggregateRating"]
                if edge["node"]["title"]["ratingsSummary"] is not None
                else None
            ),
            genres=(
                edge["node"]["title"]["titleGenres"].get("genres", [])
                if edge["node"]["title"]["titleGenres"] is not None
                else None
            ),
            runtime=(
                edge["node"]["title"]["runtime"]["seconds"]
                if edge["node"]["title"]["runtime"] is not None
                else None
            ),
        )


def is_id_none(data):
    for movie in data:
        if movie.id is None:
            return True
    return False


def main(url: str, params: dict, headers: dict, logger):
    start_time = time.time()
    end_cursor = None
    movie_details = {}
    for i in range(1000):
        json_data, end_cursor = get_json(
            url=url, params=params, headers=headers, end_cursor=end_cursor
        )
        
        if is_id_none(extract_movies(json_data)):
            raise Exception(f"Batch {i} has null id movie..")
        
        for movie in extract_movies(json_data):
            movie_details[movie.id] = movie.to_dict()

        logger.debug(f"batch: {i}, n_movies_so_far: {len(movie_details)}, time_so_far: {time.time() - start_time}")
    
    dump_location = str(Path(os.getcwd(), "..", "data", "data.json"))
    with open(dump_location, "w") as file:
        json.dump(movie_details, file, indent=4)

    return movie_details


if __name__ == "__main__":
    logger = logging.getLogger("logger")
    logger.setLevel(logging.WARNING)
    main(URL, params=params, headers=headers, logger=logger)
