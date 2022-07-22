from turtle import color
import folium as fo
import json

from matplotlib.pyplot import fill     kyochon_geo

map_Kyochon = fo.Map(location=[37.3754977,126.6332532],zoom_start=20)

fo.Circle(location=[37.3754977,126.6332532],
          radius=100,
          color='orange',
          fill=False,
          popup='인천대'  
).add_to(map_Kyochon)

jf = open(kyochon_geo.cs)





map1.save('map1.html')
