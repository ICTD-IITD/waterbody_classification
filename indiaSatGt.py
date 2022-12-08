import pandas as pd
# # import Ma

import datetime  


# data = pd.read_csv('Testing2.csv')

# dt_months = data.drop(columns=['geox', 'geoy'])

# print(dt_months)

# dt_months = dt_months.fillna(dt_months.mean(axis=0),axis= 0)

# # # dt = dt.dropna()
# dt_months.to_csv("Testing3.csv")

data = pd.read_csv('IndiaSat_Water_S2_new.csv')
# print(data.head())


# df = 

data = data[['NDWI', 'geox', 'geoy', 'timestamp']]


data['month'] = pd.to_datetime(data['timestamp'], unit='ms')
data['month'] = data['month'].dt.strftime('%m-%d')

data = data[['NDWI', 'geox', 'geoy', 'month']]

data = data.groupby(['geox', 'geoy','month']).mean()


dt = data.pivot_table('NDWI', ['geox','geoy'], 'month')

print(dt)

# dt_months = dt.drop(columns=['geox', 'geoy'])

# dt_months = dt_months.fillna(dt_months.mean(axis=0),axis= 0)

# # dt = dt.dropna()
dt.to_csv("Testing2.csv")

dat_n = pd.read_csv('Testing2.csv')
dt_months = dat_n.drop(columns=['geox', 'geoy'])

# for row in dt_months:
# for i in range(0,len(dt_months['geox']))''
    
# dt_months = dt_months.T
# dt_months = dt_months.fillna(dt_months.mean())
# dt_months = dt_months.T
# dt_months.to_csv("Testing3.csv")
# l = data.timestamp.unique()

# print(l)
# o = []

# for v in l:
#     try:
#         o.append(datetime.datetime.fromtimestamp( v ))
#     except:
#         pass

# print(o)

# try:
    
#     l = [datetime.datetime.fromtimestamp( epoch_time/1000.0 )  for epoch_time in l]
# except:
#     pass

# print(len(l))

# print(data.head())

# dt = data.pivot_table('NDWI', ['geox','geoy'], 'timestamp')
# dt = dt.dropna()
# dt.to_csv("Testing.csv")


# unique_coord  = data.geo.unique()

# cord_df = data[data['geo'] == unique_coord[0]] 

# print(cord_df)
# for coord in 

# data['lat'] = data['.geo']
# data['long'] = data['.geo']
# data['coordinates'] = data['.geo']
# data = data.dropna()

# ndwi_dict = {}

# for i in range(len(data['.geo'])):
# 	cm_pos = 0
# 	# print(data[])
# 	for comma_pos in range(48, len(data['lat'][i])):
# 		if data['lat'][i][comma_pos] == ',':
# 			cm_pos = comma_pos
# 			break
# 	latitude = float(data['lat'][i][48: comma_pos])
# 	longitude = float(data['long'][i][comma_pos+1: len(data['long'][i])-2])

# 	if not ((latitude, longitude) in ndwi_dict.keys()):
# 		ndwi_dict[(latitude, longitude)] = [] 
# 	ndwi_dict[(latitude, longitude)].append(data['NDWI'][i])



# data_lst = []
# max_data_len = 0
# for lat_long in ndwi_dict.keys():
# 	temp_lst = []
# 	latitude, longitude = lat_long
# 	temp_lst.append(latitude)
# 	temp_lst.append(longitude)
# 	max_data_len = max(max_data_len, len(ndwi_dict[lat_long]))
# 	for ndwi in ndwi_dict[lat_long]:
# 		temp_lst.append(ndwi)

# 	data_lst.append(temp_lst)

# columns = ['latitude', 'longitude']

# for i in range(0, max_data_len):
# 	columns.append('time '+str(i))

# print(len(columns))
# print(len(data_lst))
# # print(data_lst)
# df = pd.DataFrame(data_lst, columns)

# # df.to_csv('Sentinel_water_body_ground_truth_ts.csv')
# # data = data[['coordinates', 'NDWI', 'timestamp']]

# # coordinate_list = data['coordinates'].unique()


# # data_lst = []
# # for coord in coordinate_list:

# # 	temp_lst = []
# # 	temp_data = data[data['coordinates']== coord]
# # 	print(temp_data['NDWI'])
# # 	# temp_data.append(coord)
# # 	temp_lst.append(coord)
# # 	for ndwi in temp_data['NDWI']:
# # 		temp_lst.append(ndwi)
# # 	# print(f"{latitude} {longitude}")

# # 	data_lst.append(temp_lst)

# # print(data_lst)
# # {"geodesic":false,"type":"Point","coordinates":[80.890180656384,17.858598838580054]}


# import pandas as pd
# import datetime  

# data = pd.read_csv('IndiaSat_Water_S2_new.csv')

# data = data[['NDWI', 'geox', 'geoy', 'timestamp']]
# data['month'] = pd.to_datetime(data['timestamp'], unit='ms')
# data['month'] = pd.DatetimeIndex(data['month']).month

# data = data[['NDWI', 'geox', 'geoy', 'month']]
# data = data.groupby(['geox', 'geoy','month']).mean()


# dt = data.pivot_table('NDWI', ['geox','geoy'], 'month')
# dt.to_csv("Testing2.csv")