import pandas #0.20.1
import urllib2 #2.7

def fetch_data(sensor_type, sensor_id, dates):
    """ 
    :param sensor_type: eg sds011, dht222, dht11
    :param sensor_id: sensor ID as registered with http://api.airquality.codeforafrica.org/ e.g  40
    :param dates: list of str dates e.g ["2018-01-01", "2018-01-02",......, "2018-01-30"]
    :return: pandas.core.frame.DataFrame object that can be written to a csv file 
    example: data = fetch_data("sds011", 27, ["2018-06-01", "2018-06-02", "2018-06-11", "2018-06-19"])
    Note that timestamp is UTC
    """""
    def fetch(sensor_type, sensor_id):
        def f(date):
            data = pandas.DataFrame()
            try:
                data = data.append(
                    pandas.read_csv("http://archive.sensors.africa/archive/{}/{}_{}_sensor_{}.csv".format(date, date, sensor_type, sensor_id), sep=";")
                )
            except urllib2.HTTPError:
                pass
            return data
        return f

    return reduce(lambda x, y: x.append(y),
           map(fetch(sensor_type, sensor_id), dates))