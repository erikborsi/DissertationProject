# Import all the tools needed
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Read in the CSV file in and create a DataFrame
vgs_df = pd.read_csv("data/vgsales.csv", header=0, sep=",")

# Presentation in the console
pd.options.display.max_columns = False
pd.options.display.expand_frame_repr = False


# Print out the whole DataFrame with the print() method
def printTheWholeDataFrame(dataframe):
    print(dataframe)


# printTheWholeDataFrame(vgs_df)


# Print out the head of the DataFrame with the head() method
def printTheHeadOfTheDataFrame(dataframe, quantity):
    print(dataframe.head(quantity))


# printTheHeadOfTheDataFrame(vgs_df, 10)


# Print out the end of the DataFrame with the tail() method
def printTheEndOfTheDataFrame(dataframe, quantity):
    print(dataframe.tail(quantity))


# printTheEndOfTheDataFrame(vgs_df, 10)


# Print out the info of the DataFrame with the info() method
def printTheInfoOfTheDataFrame(dataframe):
    dataframe.info()


# printTheInfoOfTheDataFrame(vgs_df)


# Print out the description of the DataFrame with the describe() method
def printTheDescriptionOfTheDataFrame(dataframe):
    print(dataframe.describe())


# printTheDescriptionOfTheDataFrame(vgs_df)


# Print the percentile for the Japanese sales
def JapaneseSalesDataTest(dataframe):
    sales = dataframe["JP_Sales"]
    percentile62 = np.percentile(sales, 62)
    percentile63 = np.percentile(sales, 63)
    print(percentile62)
    print(percentile63)


# JapaneseSalesDataTest(vgs_df)
