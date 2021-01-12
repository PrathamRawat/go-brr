from pytrends.request import TrendReq
import pandas
import datetime

# List of keywords to search trends for
TRENDS = [
    "recession",
    "stock-market",
    "stocks",
    "money",
    "banking",
    "technology",
    "disease",
    "health",
    "sports",
    "finance",
    "election",
    "law",
    "immigration",
    "betting",
    "vaccine",
    "fire",
    "lawsuit",
    "news",
    "prayers",
    "politics",
    "mortgage",
    "rent",
    "investment",
    "forex",
    "executive order",
    "supreme court",
    "wall street",
    "wall street bets",
    "spy",
    "S&P 500",
    "NYSE",
    "NASDAQ",
    "bankruptcy",
    "unemployment",
    "gold",
    "bonds",
    "etf",
    "hedge fund",
    "luxury",
    "division",
    "silicon valley",
    "startup",
    "loan",
    "interest rates",
    "stimulus",
    "fed",
    "federal reserve",
    "default",
    "debt",
    "investor confidence",
    "debt ceiling",
    "GDP",
    "economy",
    "earnings",
    "investment banking",
    "dividends",
    "treasury",
    "venture capital",
    "jobs",
    "inflation",
    "prices",
    "billionaire",
    "millionaire",
    "analyst",
    "republican",
    "democrat",
    "fraud",
    "sec investigation",
    "bull market",
    "bear market",
    "stock trading",
    "insider trading",
    "rigged economy",
    "war",
    "government spending",
    "bailout",
    "innovation",
    "stock futures",
    "option call",
    "option put"
]


def get_session():
    return TrendReq(hl='en-US', tz=300)


def store_historical_trends():
    now = datetime.datetime.now()
    for trend in TRENDS:
        print("Gettting data for " + trend)
        data = get_session().get_historical_interest(
            ["trend"],
            year_start=2004,
            month_start=1,
            day_start=1,
            hour_start=0,
            year_end=now.year,
            month_end=now.month,
            day_end=now.day,
            hour_end=now.hour,
            sleep=60
        )
        data.to_csv("csv/" + trend + ".csv")


# def normalize_downloaded_data():
#     for trend in TRENDS:
#         file = open("csv/{}.csv".format(trend), "r")
#         data = file.read()
#         dataframe = pandas.read_csv(data)
#         for value in dataframe:


