import eda

eda.printTheInfoOfTheDataFrame(eda.vgs_df)


def RemoveEmptyCells(dataframe):
    dataframe.dropna(inplace=True)


RemoveEmptyCells(eda.vgs_df)


def DeleteTheNotNeededColumns(dataframe):
    del dataframe["Rank"]
    del dataframe["JP_Sales"]
    del dataframe["Publisher"]
    del dataframe["Year"]


DeleteTheNotNeededColumns(eda.vgs_df)


def RemoveZeroSales(dataframe):
    dataframe.dropna(subset=["NA_Sales", "EU_Sales", "Other_Sales", "Global_Sales"])


RemoveZeroSales(eda.vgs_df)


def DeleteLowAmountOfSalesOfTheGlobalSales(dataframe):
    for x in dataframe.index:
        if dataframe.loc[x, "Global_Sales"] < 1:
            dataframe.drop(x, inplace=True)
    return dataframe


DeleteLowAmountOfSalesOfTheGlobalSales(eda.vgs_df)


def RemoveDuplicates(dataframe):
    dataframe.drop_duplicates(inplace=True)


RemoveDuplicates(eda.vgs_df)


eda.printTheInfoOfTheDataFrame(eda.vgs_df)

exit()
