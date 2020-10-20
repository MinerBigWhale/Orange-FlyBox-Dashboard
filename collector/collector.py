
from influxdb import InfluxDBClient
from influxdb import SeriesHelper
from xml.etree import ElementTree
import requests
import time

# InfluxDB connections settings
host = "localhost"
port = 8086
user = "root"
password = "root"
dbname = "flybox"

client = InfluxDBClient(host, port, user, password, dbname)

# Uncomment the following code if the database is not yet created
#client.create_database(dbname)
#client.create_retention_policy("stats", "26w", 1, default=True) # nearly 6 months

class CollectorSeriesHelper(SeriesHelper):
    """Instantiate SeriesHelper to write points to the backend."""

    class Meta:
        """Meta class stores time series helper configuration."""

        client = client
        series_name = "collector"
        fields = ["upload", "download", "estimated", "duration", "percent", "limit"]
        tags = ["source"]
        retention_policy = "stats"
        bulk_size = 1 #every 1 are automaticaly send
        autocommit = True


class SimpleXmlParser:

    @staticmethod
    def get_child(element):
        childs = {}
        for child in element:
            if child:
                childs[child.tag] = SimpleXmlParser.get_child(child)
            else:
                childs[child.tag] = child.text
        return childs

    @staticmethod
    def parse(text):
        xml = ElementTree.fromstring(text)
        return SimpleXmlParser.get_child(xml)


def get_limit():
    url = "http://192.168.1.1/api/monitoring/start_date"
    response = requests.get(url)
    xml = SimpleXmlParser.parse(response.content)
    return {
        "start" : int(xml["StartDay"]),
        "limit" : float(xml["trafficmaxlimit"]) /1024/1024/1024
    }

def get_usage():
    url = "http://192.168.1.1/api/monitoring/month_statistics"
    response = requests.get(url)
    xml = SimpleXmlParser.parse(response.content)
    return {
        "download" : float(xml["CurrentMonthDownload"]) /1024/1024/1024,
        "upload" : float(xml["CurrentMonthUpload"]) /1024/1024/1024,
        "duration" : float(xml["MonthDuration"])
    }


"""Starting the loop"""
while True:
    usage = get_usage()
    limit = get_limit()
    usage["total"] = usage["download"] + usage["upload"]
    limit["percent"] = ((usage["download"] + usage["upload"]) / limit["limit"])*100
    usage["estimated"] = (usage["download"] + usage["upload"]) /usage["duration"] * (31*86400)
    print(usage)
    print(limit) 
    CollectorSeriesHelper(
        source="monitoring", 
        upload=usage["upload"], 
        download=usage["download"],
        estimated=usage["estimated"],
        duration=usage["duration"],
        percent=limit["percent"],
        limit=limit["limit"]
        )
    CollectorSeriesHelper.commit()
    print ("ZZzz...")
    time.sleep(60) # repeat every minutes