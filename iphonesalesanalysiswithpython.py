# For the iPhone sales analysis task, I have collected a dataset  containing data about the sales of iPhones in India on Flipkart. It will be an ideal dataset to analyze the sales of iPhones in India. You can download the dataset from video description.
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
sharaddata = pd.read_csv("apple_products.csv")
#print(sharaddata.head())
#print(sharaddata.isnull().sum())
#print(sharaddata.describe())

highest_rated=sharaddata.sort_values(by=["Star Rating"], ascending=False)
highest_rated= highest_rated.head(10)
#print(highest_rated['Product Name'])
""" iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated, x=label, y=counts, title="Number of ratings of highest Rated Iphone")
figure.show() 

iphone=highest_rated['Product Name'].value_counts()
label=iphone.index
counts=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated, x=label, y=counts, title="Number of Reviews of highest Rated Iphone")
figure.show()

figure=px.scatter(data_frame=sharaddata, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", trendline="ols", title="Relationship between sale price and number of ratings of iphones")
figure.show()"""

figure=px.scatter(data_frame=sharaddata, x="Number Of Ratings", y="Discount Percentage", size="Sale Price", trendline="ols", title="Relationship between Discount Percentage and number of ratings of iphones")
figure.show()


