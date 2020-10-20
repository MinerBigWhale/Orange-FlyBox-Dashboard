
from influxdb import InfluxDBClient
from influxdb import SeriesHelper
from xml.etree import ElementTree

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

"""Starting the loop"""
while True:
    CollectorSeriesHelper(
        source="monitoring", 
        )
    CollectorSeriesHelper.commit()
    print ("ZZzz...")
    time.sleep(60) # repeat every minutes