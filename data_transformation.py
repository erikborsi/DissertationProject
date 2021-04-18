import eda

eda.printTheInfoOfTheDataFrame(eda.vgs_df)

# Remove empty rows
def RemoveEmptyCells(dataframe):
    dataframe.dropna(inplace=True)

# Delete the columns that are not needed
def DeleteTheNotNeededColumns(dataframe):
    del dataframe["Rank"]
    del dataframe["JP_Sales"]
    del dataframe["Publisher"]
    del dataframe["Year"]

# Remove the rows of games that has no sales in all the columns
def RemoveZeroSales(dataframe):
    dataframe.dropna(subset=["NA_Sales",
                             "EU_Sales",
                             "Other_Sales",
                             "Global_Sales"],
                     inplace=True)

# Delete the rows that did not reach 1 million sales on the global scale
def DeleteLowAmountOfSalesOfTheGlobalSales(dataframe):
    for x in dataframe.index:
        if dataframe.loc[x, "Global_Sales"] < 1:
            dataframe.drop(x, inplace=True)
    return dataframe

# Remove duplicates from the leftover
def RemoveDuplicates(dataframe):
    dataframe.drop_duplicates(inplace=True)


RemoveEmptyCells(eda.vgs_df)
DeleteTheNotNeededColumns(eda.vgs_df)
RemoveZeroSales(eda.vgs_df)
DeleteLowAmountOfSalesOfTheGlobalSales(eda.vgs_df)
RemoveDuplicates(eda.vgs_df)

eda.printTheInfoOfTheDataFrame(eda.vgs_df)
