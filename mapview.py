#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:29:24 2020

@author: fidelismwansa
"""

import folium
import shelve 

# Map all devices on the map 
db = shelve.open('devices.db')

# United Kingdom Coordinates
m = folium.Map(
    location=[52.3555, 1.1743],
    zoom_start=13,
    tiles='Stamen Terrain'
)

for x in db:
    # Get coordinates
    cords = db[x]['geometry']['coordinates']
    # Get Name 
    name = x
    #Get Alert Status
    colour = ""
    if db[x]['Status'] ==  True:
        colour = "red"
    else:
        colour = "blue"
    # Append the coordiantes 
    folium.Marker(
        location=[cords[0], cords[1]],
        popup= str(x),
        icon=folium.Icon(color=colour, icon='info-sign')
    ).add_to(m)
#print(db['VEDA-1']['geometry']['coordinates'])
'''
folium.Marker(
    location=[45.3300, -121.6823],
    popup='Some Other Location',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)
'''
m.save('index.html')
