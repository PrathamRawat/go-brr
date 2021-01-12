import pandas as pd
import datetime
import time


def clean_csv(filename):
    data = open("../csv/{}.csv".format(filename))
    dataframe = pd.read_csv(data)
    data.close()
    dataframe = dataframe.drop('isPartial', axis=1)
    dataframe = dataframe.apply(lambda x: [int(time.mktime(datetime.datetime.strptime(x['date'], "%Y-%m-%d %H:%M:%S").timetuple())), x['stimulus']], axis=1, result_type='broadcast')
    return dataframe
