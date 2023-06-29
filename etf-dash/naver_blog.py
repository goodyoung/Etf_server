import sys
import time
import json
import re
import html # html 특수 문자 -> 원래 문자로

import requests
from requests.utils import quote


# title과 description내의 태그 제거
def remove_tag(html_text):
    """태그 제거용 함수"""
    
    tag_pattern = re.compile(r"<[^>]+>")
    return tag_pattern.sub('', html.unescape(html_text))


def naver_blog_search(client_id, client_secret, keyword, start=1, display=100):
    """naver search api 에 검색어를 보내 결과를 얻는다.
    """
    
    headers = {
        "X-Naver-Client-Id" : client_id,
        "X-Naver-Client-Secret" : client_secret
    }

    # start = start + 1 if start > 1 else start
    
    # 최대 1회 검색 display=100
    result = []
    for i in range(1, start+1):
        # json 결과
        # disply=100 최대 
        # start=1~100 최대
        blog_search = f"https://openapi.naver.com/v1/search/blog?query={quote(keyword)}&display=100&start={i}"
        # print(blog_search)
        
        response = requests.get(blog_search, headers=headers)

        if(response.status_code==200):
            result.append(response.text)
        else:
            print("Error Code:" + str(response.status_code))
            result.append(f'{keyword} : {str(response.status_code)}')

    items = []
    for i in range(0, len(result)):
        items.append( json.loads(result[i])['items'] )   
    return items


def concat_blog_description(items):
    """여러개의 검색 ㄱ결과를 가진 items 를 받아 하나의 문자열로 결합한다."""
    blog_list = []
    for item_list in items:
        for item in item_list:
            content = {
                "title": remove_tag(item['title']),
                "link": item['link'],
                "description": remove_tag(item['description'])
            }
            blog_list.append(content)

    contents = [item['description'] for item in blog_list ]
    contents = ",".join(contents)
    return contents
