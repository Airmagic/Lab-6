# This is a pip install
import folium

# this is a map location
map_mn = folium.Map(location = [45, -93.2], zoom_start = 13)

# adding a marker to the map for MCTC
folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)

# saving this to the map
map_mn.save("map.html")
