from pytrends.request import TrendReq
import pandas as pd
import datetime
import time

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


def normalize_data(filename):
    data = open("csv/{}.csv".format(filename))
    dataframe = pd.read_csv(data)
    data.close()
    dataframe = dataframe.drop('isPartial', axis=1)
    dataframe = dataframe.apply(lambda x: [int(time.mktime(datetime.datetime.strptime(x['date'], "%Y-%m-%d %H:%M:%S").timetuple())), x['trend']], axis=1, result_type='broadcast')
    dataframe['change'] = dataframe['trend'].pct_change()
    return dataframe


def get_training_dataframes():
    output = dict()
    for trend in TRENDS:
        print("Normalizing {}".format(trend))
        output['trend'] = normalize_data(trend)
    return output
