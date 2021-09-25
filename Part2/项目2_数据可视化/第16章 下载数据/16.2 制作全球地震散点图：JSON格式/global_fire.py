import csv
import plotly.express as px
import pandas as pd

filename = './data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    lat_index= header_row.index('latitude')
    lon_index = header_row.index('longitude')
    brightness_index = header_row.index('brightness')
    lats, lons, brightness = [], [], []
    for row in reader:
        lats.append(float(row[lat_index]))
        lons.append(float(row[lon_index]))
        brightness.append(float(row[brightness_index]))

data = pd.DataFrame(
    data=zip(lons, lats, brightness), columns=["经度", "纬度", "火灾强度"]
)
data.head()

fig = px.scatter(

    data,
    x="经度",
    y="纬度",
    labels={'x':"经度", 'y':"纬度"},
    range_x=[-200, 200],
    range_y=[-90, 90],

    width=800,
    height=800,

    title="全球火灾信息",
    size='火灾强度',
    size_max=10,
    color='火灾强度',

)
fig.write_html("world_fires.html")
fig.show()
