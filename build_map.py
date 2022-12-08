import folium
import webbrowser

m = folium.Map(location=[-3.149273, -60.040787],
               tiles="Stamen Terrain", zoom_start=6)

folium.Marker(
    location=[-3.149273, -60.040787],
    popup= " <i> Cidade de Manaus \n Amazonas <i\>",
    icon=folium.Icon(color="gray", icon_color="red", icon="fire"),
    tooltip="Clique aqui!"
).add_to(m)

m.save("show-map.html")

webbrowser.open_new_tab("show-map.html")

