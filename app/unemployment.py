

print("UNEMPLOYMENT REPORT...")


import os

from app.alphavantage_service import fetch_unemployment_data


parsed_response = fetch_unemployment_data()

data = parsed_response["data"]
latest = data[0]
print(latest) #> {'date': '2022-02-01', 'value': '3.8'}


#exit()

#
# DATA AND CHARTING
#

from pandas import DataFrame
from plotly.express import bar


df = DataFrame(data)
print(df.head())

# new column as float version of original strings column
df["unemployment_rate"] = df["value"].astype(float)

# remove original column to clean up
df.drop(columns=["value"], inplace=True)


fig = bar(df, x="date", y="unemployment_rate", title="Unemployment Rates")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html

# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.update_yaxes
# https://plotly.com/python/reference/layout/yaxis/
# https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-ticksuffix
fig.update_yaxes(
    #tickprefix="$",
    ticksuffix="%",
    showgrid=True,
    title_text="Unemployment Rates"
)

fig.update_xaxes(
    title_text="Dates"
)

fig.show()

#breakpoint()


print("DATAVIZ EXPORT...")
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html#plotly.graph_objects.Figure.to_image
# fig.to_image(format="png")

# https://plotly.com/python/static-image-export/
# Image export using the "kaleido" engine requires the kaleido package,
#which can be installed using pip:
#    $ pip install -U kaleido
img_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.png")
fig.write_image(img_filepath)


print("CSV EXPORT...")
csv_filepath = os.path.join(os.path.dirname(__file__), "..", "reports", "unemployment.csv")
df.to_csv(csv_filepath, index=False)
