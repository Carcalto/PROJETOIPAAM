import folium
import webbrowser

m = folium.Map(location=[-3.149273, -60.040787],
               tiles="Stamen Terrain", zoom_start=7)

folium.Marker(
    location=[-3.149273, -60.040787],
    popup="Cidade de Manaus",
    icon=folium.Icon(color="green"),
).add_to(m)

m.save("index.html")

webbrowser.open_new_tab("index.html")

