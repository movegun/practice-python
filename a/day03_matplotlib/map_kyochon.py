import pandas as pd
import folium as fo

k_csv = pd.read_csv('자료실//kyochon_geo.csv')

#print(k_csv.head(5))

x = []
y = []

for i in range(len(k_csv['x'])):
    x.append(k_csv['x'][i])
    y.append(k_csv['y'][i])
    
#print(len(x))
#print(len(y))

map_kyochon = fo.Map(location=[x[1],y[1]],zoom_start=14)

for i in range(len(x)):
    fo.Marker([x[i],y[i]],popup='교촌_%d호점'%i,icon=fo.Icon(color='red',icon='info-sign')).add_to(map_kyochon)

map_kyochon.save('kyochon_Location.html')