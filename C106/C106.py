import numpy as np
import plotly.express as px
import csv

def getDataSource(data_path):
    Roll_No = []
    Days_present = []
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for row in df:
            Roll_No.append(float(row["Marks In Percentage"]))
            Days_present.append(float(row["Days Present"]))
    return {"x": Roll_No,"y": Days_present}

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file) 
        fig = px.scatter(df,x = "Marks In Percentage",y="Days Present")
        fig.show()

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Marks in percentage and days present:------>",correlation[0,1])



def setup():
    data_path = 'Student Marks vs Days Present.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    # If this code not work here then try to run this code in collab sheet 
    plotFigure(data_path)

setup()

    