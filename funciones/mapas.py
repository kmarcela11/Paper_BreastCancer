import folium
from folium.features import GeoJsonTooltip

def mapa_smr_departamental(departamentos, nombre_columna, get_color, nombre_archivo):
    m = folium.Map(tiles="CartoDB positron", location=[4.5, -74], zoom_start=5)

    folium.GeoJson(
        departamentos,
        style_function=lambda feature: {
            "fillColor": get_color(feature["properties"].get("SMR")),
            "color": "black",
            "weight": 0.5,
            "fillOpacity": 0.85,
        },
        tooltip=GeoJsonTooltip(
            fields=[nombre_columna, "SMR"],
            aliases=["Departamento:", "SMR:"],
            localize=True,
            sticky=True
        )
    ).add_to(m)

    m.save(f'../map_outputs/{nombre_archivo}')
    

def mapa_tae_departamental(departamentos, nombre_columna, get_color, nombre_archivo):
    m = folium.Map(tiles="CartoDB positron", location=[4.5, -74], zoom_start=5)

    folium.GeoJson(
        departamentos,
        style_function=lambda feature: {
            "fillColor": get_color(feature["properties"].get("TAE")),
            "color": "black",
            "weight": 0.5,
            "fillOpacity": 0.85,
        },
        tooltip=GeoJsonTooltip(
            fields=[nombre_columna, "TAE"],
            aliases=["Departamento:", "TAE:"],
            localize=True,
            sticky=True
        )
    ).add_to(m)

    m.save(f'../map_outputs/{nombre_archivo}')
    

def mapa_smr_municipal(municipios, nombre_columna, get_color_smr_mun, nombre_archivo):
    m = folium.Map(tiles="CartoDB positron", location=[4.5, -74], zoom_start=5)

    folium.GeoJson(
        municipios,
        style_function=lambda feature: {
            "fillColor": get_color_smr_mun(feature["properties"].get("TAE")),
            "color": "black",
            "weight": 0.5,
            "fillOpacity": 0.85,
        },
        tooltip=GeoJsonTooltip(
            fields=[nombre_columna, "SMR"],
            aliases=["Municipio:", "SMR:"],
            localize=True,
            sticky=True
        )
    ).add_to(m)

    m.save(f'../map_outputs/{nombre_archivo}')