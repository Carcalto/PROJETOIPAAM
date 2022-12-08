import folium
import webbrowser

m = folium.Map(location=[-3.149273, -60.040787],
               tiles="Stamen Terrain", zoom_start=6)

folium.Marker(
    location=[-3.149273, -60.040787],
    popup= " <i> Cidade de Manaus\AM <i\>",
    icon=folium.Icon(color="green", icon_color="red", icon="fire"),
    tooltip="Clique aqui!"
).add_to(m)

folium.Marker(
    location=[-1.182210, -62.828748],
    popup= " <i> Cidade de Barcelos/AM <i\>",
    icon=folium.Icon(color="blue", icon_color="white", icon="ok-circle"),
    tooltip="Clique aqui!"
).add_to(m)

folium.Marker(
    location=[-7.302706, -63.142652],
    popup= " <i> Cidade de Humaitá/AM <i\>",
    icon=folium.Icon(color="orange", icon_color="green", icon="leaf"),
    tooltip="Clique aqui!"
).add_to(m)

folium.Marker(
    location=[-2.754250, -66.775091],
    popup= " <i> Cidade de Jutaí/AM <i\>",
    icon=folium.Icon(color="white", icon_color="red", icon="remove-circle"),
    tooltip="Clique aqui!"
).add_to(m)

m.save("show-map.html")

webbrowser.open_new_tab("show-map.html")

