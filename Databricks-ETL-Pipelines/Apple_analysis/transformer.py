# Databricks notebook source
from pyspark.sql import Window
from pyspark.sql.functions import lead, col, broadcast,collect_set, size, array_contains


class Transformer:
    def __init__(self):
        pass
    def transform(self, inputDFs):
        pass

class AirpodsAfterIphoneTransformer(Transformer):
    def transform(self, inputDFs):
        """
        Customers bought Airpods after iphone purchase
        """

        transactionInputDF = inputDFs.get("transactionInputDF")

        print("transactionInputDF in transform")

        transactionInputDF.show()

        windowSpec = Window.partitionBy("customer_id").orderBy("transaction_date")

        transformedDF = transactionInputDF.withColumn(
            "next_product_name", lead("product_name").over(windowSpec)

        )

        print("Airpods after buying iphone")
        transformedDF.orderBy("customer_id","transaction_date","product_name").show()

        
        filteredDF = transformedDF.filter(
            (col('product_name') == "iPhone") & (col("next_product_name") == "AirPods")
        )

        filteredDF.orderBy("customer_id", "transaction_date", "product_name").show()


        customerInputDF = inputDFs.get("customerInputDF")


        joinDF = customerInputDF.join(
            broadcast(filteredDF),
            "customer_id"
        )
        print ("Joined dataframe")
        joinDF.select(
            "customer_id",
            "customer_name",
            "location",
            "product_name",
            "next_product_name"
        ).show()

        return joinDF



class  OnlyAirpodsAndIphone(Transformer):
     def transform(self, inputDFs):
        """
        Customers only bought Airpods and iphone 
        """

        transactionInputDF = inputDFs.get("transactionInputDF")

        groupedDF = transactionInputDF.groupBy("customer_id").agg(
            collect_set("product_name").alias("products")
        )

        print("Grouped DF")


        groupedDF.show()

        filteredDF = groupedDF.filter(

            
            (array_contains(col("products"), "iPhone")) &
            (array_contains(col("products"), "AirPods")) & 
            (size(col("products")) == 2)
        )

        print("Only airpods and iphone")

        filteredDF.show()

        customerInputDF = inputDFs.get("customerInputDF")

        

        joinDF = customerInputDF.join(
            broadcast(filteredDF),
            "customer_id"
        )
        print ("Joined dataframe")
        joinDF.select(
            "customer_id",
            "customer_name",
            "location",
            "products"
        ).show()

        return joinDF




        


