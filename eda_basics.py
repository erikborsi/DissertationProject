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


def printTheWholeDataFrame(dataframe):
    # Print out the whole DataFrame with the print() method
    print("START OF THE METHOD " + 30 * "-" + " START OF THE METHOD")
    print(dataframe)
    print("END OF THE METHOD " + 35 * "-" + " END OF THE METHOD")


# printTheWholeDataFrame(vgs_df)


def printTheHeadOfTheDataFrame(dataframe, quantity):
    # Print out the head of the DataFrame with the head() method
    print("START  OF THE METHOD " + 30 * "-" + " START OF THE METHOD")
    print(dataframe.head(quantity))
    print("END OF THE METHOD " + 35 * "-" + " END OF THE METHOD")


printTheHeadOfTheDataFrame(vgs_df, 10)


def printTheEndOfTheDataFrame(dataframe, quantity):
    # Print out the end of the DataFrame with the tail() method
    print("START OF THE METHOD " + 30 * "-" + " START OF THE METHOD")
    print(dataframe.tail(quantity))
    print("END OF THE METHOD " + 35 * "-" + " END OF THE METHOD")


printTheEndOfTheDataFrame(vgs_df, 10)


def printTheInfoOfTheDataFrame(dataframe):
    # Print out the info of the DataFrame with the info() method
    print("START  OF THE METHOD " + 30 * "-" + " START OF THE METHOD")
    dataframe.info()
    print("END OF THE METHOD " + 35 * "-" + " END OF THE METHOD")


# printTheInfoOfTheDataFrame(vgs_df)


def printTheDescriptionOfTheDataFrame(dataframe):
    # Print out the description of the DataFrame with the describe() method
    print("START  OF THE METHOD " + 30 * "-" + " START OF THE METHOD")
    print(dataframe.describe())
    print("END OF THE METHOD " + 35 * "-" + " END OF THE METHOD")


# printTheDescriptionOfTheDataFrame(vgs_df)


exit()
