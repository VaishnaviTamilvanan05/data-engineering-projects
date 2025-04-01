# Databricks notebook source
# MAGIC %run "./extractor"
# MAGIC

# COMMAND ----------

# MAGIC %run "./transformer"
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC
# MAGIC %run "./Loader"
# MAGIC

# COMMAND ----------

class FirstWorkFlow:
    """
    ETL pipeline generates the data of all customores who bought Airpods after iphone
    """
    def __init__(self):
        pass
    def runner(self):

        #Step1: Extract all data from different source
        inputDFs = AirpodsAfterIphoneExtractor().extract()
        # Step 2: Transformation to find Customers bought Airpods after iphone purchase
        firstTransformedDF = AirpodsAfterIphoneTransformer().transform(
            inputDFs

        )
        # Step 3: Load transformed data to diffrent sources
        AirpodsAfterIphoneLoader(firstTransformedDF).sink()
    





# COMMAND ----------

class SecondWorkFlow:
    """
    ETL pipeline generates the data of all customores who bought Airpods after iphone
    """
    def __init__(self):
        pass
    def runner(self):

        #Step1: Extract all data from different source
        inputDFs = AirpodsAfterIphoneExtractor().extract()
        # Step 2: Transformation to find Customers bought Airpods after iphone purchase
        onlyAirpodsAndIphoneDF = OnlyAirpodsAndIphone().transform(
            inputDFs

        )
        # Step 3: Load transformed data to diffrent sources
        OnlyAirpodsAndIphoneLoader(onlyAirpodsAndIphoneDF).sink()
    


# COMMAND ----------

class WorkFlowRunner:
    
    def __init__(self,name):
        self.name = name

    def runner(self):
        if self.name == "firstWorkFlow":
            return FirstWorkFlow().runner()
        elif self.name == "secondWorkFlow":
            return SecondWorkFlow().runner()
        else:
            return ValueError("Not implemented")

name = "secondWorkFlow"

workFlowRunner =WorkFlowRunner(name).runner()


