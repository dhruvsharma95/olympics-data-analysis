# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
#Code starts here

# Data Loading 
data = pd.read_csv(path)

data.rename(columns={'Total':'Total_Medals'}, inplace=True)

# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter'))

better_event = data['Better_Event'].value_counts().index[0]
print(data.head(10))
print(better_event)

# Top 10
top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]

top_countries.drop([146], axis=0, inplace=True)

def top_ten(df,col):
    country_list = []
    top_10 = df.nlargest(10, col)
    country_list = top_10['Country_Name'].tolist()
    return country_list

top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10 = top_ten(top_countries, 'Total_Medals')

print(top_10_summer)
print(top_10_winter)
print(top_10)
common = set(top_10).intersection(top_10_summer, top_10_winter)
print(common)

# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar', x='Country_Name', y='Total_Summer')
winter_df.plot(kind='bar', x='Country_Name', y='Total_Winter')
top_df.plot(kind='bar', x='Country_Name', y='Total_Medals')

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.sort_values(by=['Golden_Ratio'], ascending=False).values[0][0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.sort_values(by=['Golden_Ratio'], ascending=False).values[0][0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.sort_values(by=['Golden_Ratio'], ascending=False).values[0][0]

print(summer_df['Golden_Ratio'])
print(summer_max_ratio)
print(summer_country_gold)

print(winter_df['Golden_Ratio'])
print(winter_max_ratio)
print(winter_country_gold)

print(top_df['Golden_Ratio'])
print(top_max_ratio)
print(top_country_gold)

# Best in the world 
data_1 = data.drop([146], axis=0)
data_1['Total_Points'] = 3*data_1['Gold_Total'] + 2*data_1['Silver_Total'] + data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
best_country = data_1.sort_values(by=['Total_Points'], ascending=False).values[0][0]

print(most_points)
print(best_country)

# Plotting the best
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



