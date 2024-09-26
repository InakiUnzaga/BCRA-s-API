#Importaciones
import pandas as pd
import requests

#Conexión a la api BCRA // estadisticascambiarias - V1
fecha="2024-01-10"
urlMaestro= "https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Maestros/Divisas"
urlCotizaciones= f"https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Cotizaciones?fecha={fecha}"

data = requests.get(urlCotizaciones,verify=False).json()

#Creación del dataframe(..Detalle + .Fecha)
df = pd.DataFrame(data['results']['detalle'])

fecha = data["results"]["fecha"]

df["fecha"] = fecha
print(df)


