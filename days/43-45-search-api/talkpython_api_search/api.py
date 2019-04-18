from typing import List

import requests
import collections

Episodes = collections.namedtuple('Episodes',
                                  'category, id, url, title, description'
                                  )


def find_items_by_keyword(keyword: str) -> List[Episodes]:
    keyword = keyword.replace(" ", "-")
    searchUrl = f'http://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(searchUrl)
    resp.raise_for_status()

    results = resp.json()
    items = []
    for r in results.get('results'):
        items.append(Episodes(**r))

    return items
