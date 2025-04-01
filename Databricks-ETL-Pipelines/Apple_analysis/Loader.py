# Databricks notebook source
# MAGIC %run "./loader_Factory"
# MAGIC

# COMMAND ----------

class AbstractLoader:
    def __init__(self, transformedDF):
        self.transformedDF = transformedDF

    def sink(self):
        pass

class AirpodsAfterIphoneLoader(AbstractLoader):
    def sink(self):
        get_sink_source(
            sink_type = "dbfs",
            df = self.transformedDF,
            path ="/dbfs/FileStore/output",
            method = "overwrite"

        ).load_data_frame()


class OnlyAirpodsAndIphoneLoader(AbstractLoader):
    def sink(self):
        params = {
            "partitionByColumns": ["location"]
        }
        get_sink_source(
            sink_type = "dbfs_with_partition",
            df = self.transformedDF,
            path ="/dbfs/FileStore/outputetl2",
            method = "overwrite",
            params = params

        ).load_data_frame()

        get_sink_source(
            sink_type = "delta",
            df = self.transformedDF,
            path ="default.onlyAirpodsAndiphone",
            method = "overwrite",
            

        ).load_data_frame()



