#!/usr/gamma/'Python_intermediary python
# -*-coding:utf-8 -*-
'''
@File    :   test.py
@Time    :   2024/02/22 12:03:55
@Author  :   MSN 
@Version :   1.0
@Contact :   mass.zenn.2014@gmail.com
@License :   (C)Copyright 2024-2025, MSN
@Desc    :   None
'''

import requests

cookies = {
    'session-id': '133-1434679-5554117',
    'session-id-time': '2082787201l',
    'ad-oo': '0',
    'ci': 'eyJhY3QiOiJDUDZWR0lBUDZWR0lBRjRBQkNFTmZyLWdBQUFBQUFBQUFCYWdBQVFBQUFBZ0FBQUEiLCJnY3QiOiJDUDZWR0lBUDZWR0lBRjRBQkNFTkFiRWdBQUFBQUFBQUFCYWdBQVFBQUFBZ0FBRkFvQU1BQVFmUUNRQVlBQWctZ09nQXdBQkI5QWxBQmdBQ0Q2QlNBREFBRUgwQXdBR0FBSVBvQ2dBTUFBUWZRR0FBWUFBZy1nUUFBd0FCQjlBUUFQQUJBQUNRQUZRQU5ZQXdnREVBR1lBT1lBZ0FCU2dEVkFKYUFWa0Fyd0J3Z0ZoZy5ZQUFBQUFBQUFBQSIsInB1cnBvc2VzIjpbXSwidmVuZG9ycyI6W119',
    'ubid-main': '132-5455927-3384765',
    'uu': 'eyJpZCI6InV1YjIxMzFlNzkwMTQ5NGY2ZDllY2QiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=',
    'session-token': 'qTEEFxOOf2izvlPJuMKnORf0YwVSMRhSUojZCIOYgGu/bcE7sbboVqEf9xuXN0FNSYx87UmoUvlxoDE9uTlAqis4BP+VzdbnLhiGQg5S0xWTmVrIuhQOsJg8jkmkCT/fvboIs2bqoizpHTUfbZY/0N7nAcTdZ+gqmdXcspsa1PpdI56/VK9fo00S2L5xtSqfpM2pH53sOlBmG+pZoV06oscvVuuu3OWcci7awGzaXepz3zqZiBiMS/VJ0R9FGlLKjg6HR7UYU/OEpvyE0Qi+lQAiOsWxsR5Po5pyyhbhQBzOjBt392OO2KiVK76kD9HN8opA0EeWNb1buOlaoSr8Yw8brSkfNVMF',
}

headers = {
    'authority': 'caching.graphql.imdb.com',
    'accept': 'application/graphql+json, application/json',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'session-id=133-1434679-5554117; session-id-time=2082787201l; ad-oo=0; ci=eyJhY3QiOiJDUDZWR0lBUDZWR0lBRjRBQkNFTmZyLWdBQUFBQUFBQUFCYWdBQVFBQUFBZ0FBQUEiLCJnY3QiOiJDUDZWR0lBUDZWR0lBRjRBQkNFTkFiRWdBQUFBQUFBQUFCYWdBQVFBQUFBZ0FBRkFvQU1BQVFmUUNRQVlBQWctZ09nQXdBQkI5QWxBQmdBQ0Q2QlNBREFBRUgwQXdBR0FBSVBvQ2dBTUFBUWZRR0FBWUFBZy1nUUFBd0FCQjlBUUFQQUJBQUNRQUZRQU5ZQXdnREVBR1lBT1lBZ0FCU2dEVkFKYUFWa0Fyd0J3Z0ZoZy5ZQUFBQUFBQUFBQSIsInB1cnBvc2VzIjpbXSwidmVuZG9ycyI6W119; ubid-main=132-5455927-3384765; uu=eyJpZCI6InV1YjIxMzFlNzkwMTQ5NGY2ZDllY2QiLCJwcmVmZXJlbmNlcyI6eyJmaW5kX2luY2x1ZGVfYWR1bHQiOmZhbHNlfX0=; session-token=qTEEFxOOf2izvlPJuMKnORf0YwVSMRhSUojZCIOYgGu/bcE7sbboVqEf9xuXN0FNSYx87UmoUvlxoDE9uTlAqis4BP+VzdbnLhiGQg5S0xWTmVrIuhQOsJg8jkmkCT/fvboIs2bqoizpHTUfbZY/0N7nAcTdZ+gqmdXcspsa1PpdI56/VK9fo00S2L5xtSqfpM2pH53sOlBmG+pZoV06oscvVuuu3OWcci7awGzaXepz3zqZiBiMS/VJ0R9FGlLKjg6HR7UYU/OEpvyE0Qi+lQAiOsWxsR5Po5pyyhbhQBzOjBt392OO2KiVK76kD9HN8opA0EeWNb1buOlaoSr8Yw8brSkfNVMF',
    'origin': 'https://www.imdb.com',
    'referer': 'https://www.imdb.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'x-amzn-sessionid': '133-1434679-5554117',
    'x-imdb-client-name': 'imdb-web-next-localized',
    'x-imdb-client-rid': 'AK26M64XK2ZZGDJQS4R7',
    'x-imdb-user-country': 'US',
    'x-imdb-user-language': 'en-US',
    'x-imdb-weblab-treatment-overrides': '{"IMDB_DESKTOP_SEARCH_ALGORITHM_UPDATES_577300":"T1","IMDB_NAV_PRO_FLY_OUT_Q1_REFRESH_848923":"T2"}',
}

params = {
    'operationName': 'AdvancedTitleSearch',
    'variables': '{"after":"eyJlc1Rva2VuIjpbIjEyNyIsIjEyNyIsInR0Mjc5MzY3NzAiXSwiZmlsdGVyIjoie1wiY29uc3RyYWludHNcIjp7XCJjZXJ0aWZpY2F0ZUNvbnN0cmFpbnRcIjp7fSxcImNvbG9yYXRpb25Db25zdHJhaW50XCI6e30sXCJjcmVkaXRlZENvbXBhbnlDb25zdHJhaW50XCI6e30sXCJnZW5yZUNvbnN0cmFpbnRcIjp7fSxcImxpc3RDb25zdHJhaW50XCI6e1wiaW5BbGxMaXN0c1wiOltdLFwiaW5BbGxQcmVkZWZpbmVkTGlzdHNcIjpbXSxcIm5vdEluQW55TGlzdFwiOltdLFwibm90SW5BbnlQcmVkZWZpbmVkTGlzdFwiOltdfSxcInJlbGVhc2VEYXRlQ29uc3RyYWludFwiOntcInJlbGVhc2VEYXRlUmFuZ2VcIjp7fX0sXCJydW50aW1lQ29uc3RyYWludFwiOntcInJ1bnRpbWVSYW5nZU1pbnV0ZXNcIjp7fX0sXCJ0aXRsZVR5cGVDb25zdHJhaW50XCI6e1wiYW55VGl0bGVUeXBlSWRzXCI6W1wibW92aWVcIl19LFwidXNlclJhdGluZ3NDb25zdHJhaW50XCI6e1wiYWdncmVnYXRlUmF0aW5nUmFuZ2VcIjp7fSxcInJhdGluZ3NDb3VudFJhbmdlXCI6e319fSxcImxhbmd1YWdlXCI6XCJlbi1VU1wiLFwic29ydFwiOntcInNvcnRCeVwiOlwiUE9QVUxBUklUWVwiLFwic29ydE9yZGVyXCI6XCJBU0NcIn0sXCJyZXN1bHRJbmRleFwiOjQ5fSJ9","certificateConstraint":{},"colorationConstraint":{},"creditedCompanyConstraint":{},"first":50,"genreConstraint":{},"listConstraint":{"inAllLists":[],"inAllPredefinedLists":[],"notInAnyList":[],"notInAnyPredefinedList":[]},"locale":"en-US","releaseDateConstraint":{"releaseDateRange":{}},"runtimeConstraint":{"runtimeRangeMinutes":{}},"sortBy":"POPULARITY","sortOrder":"ASC","titleTypeConstraint":{"anyTitleTypeIds":["movie"]},"userRatingsConstraint":{"aggregateRatingRange":{},"ratingsCountRange":{}}}',
    'extensions': '{"persistedQuery":{"sha256Hash":"e7a1c7b10a7a9765731e5c874cef0342dfbd0dd7a87fa796e828778e54a07a20","version":1}}',
}

response = requests.get('https://caching.graphql.imdb.com/', params=params, cookies=cookies, headers=headers)
print( response.json())