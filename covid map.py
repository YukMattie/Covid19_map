#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd 
import numpy as np 
import folium
from folium.plugins import HeatMap

df = pd.read_csv("dataset.csv")
m = folium.Map(tiles = 'Stamen Terrain',min_zoom = 1.5)
# display(m)


# In[12]:


url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes = f'{url}/world-countries.json'
folium.Choropleth(
    geo_data = country_shapes,
    min_zoom=2,
    name='Covid-19',
    data=df,
    columns=['Country', 'Confirmed'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    nan_fill_color='black',
    legend_name = 'Total Confirmed COVID cases',
).add_to(m)
display(m)


# In[13]:


def plotDot(point):
    folium.CircleMarker(location = (point.latitude, point.longitude),
                       radius = 5,
                       weight = 2,
                       popup = [point.Country, point.Confirmed, point.Recovered],
                       fill_color = '#000000').add_to(m)
df.apply(plotDot, axis = 1)
m.fit_bounds(m.get_bounds())
display(m)


# In[ ]:




