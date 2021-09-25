import json

# 探索数据的结构
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) # json.load()将数据转换为Python能够处理的格式（字典）

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4) # json.dump()接受一个JSON数据对象和一个文件对象，并将数据写入这个文件中，indent=4让dump()使用与数据结构匹配的缩进量来设置数据格式

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])