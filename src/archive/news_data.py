import datetime
import pynytimes

API_KEY = open("nyt_api_key.txt", "r").read()

def get_client():
    return pynytimes.NYTAPI(API_KEY, https=False)


def get_news(date: datetime):
    return get_client().article_search(
        results=100,
        dates={
            "begin":date,
            "end":date
        },
        options={
            "sort": "newest",
        }
    )


def get_politics_news():


