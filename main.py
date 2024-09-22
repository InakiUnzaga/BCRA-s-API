import pandas as pd
import requests

Numero="2024-09-20"
fecha= f"fecha={Numero}"

urlMaestro= "https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Maestros/Divisas"
urlCotizaciones= f"https://api.bcra.gob.ar/estadisticascambiarias/v1.0/Cotizaciones?{fecha}"


data = requests.get(urlCotizaciones,verify=False).json()

