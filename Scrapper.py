import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

start_id = 1409 #Fecha inicial
end_id = 4460  # puedes ajustar el rango
all_tables = []

for prueba_id in range(start_id, end_id + 1):
    url = f"https://sistemainfo.fedesgrimacolombia.com/resultados?prueba={prueba_id}"
    print(f"📄 Revisando: {url}")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Error {response.status_code} en la página {prueba_id}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # --- Extraer título y fecha ---
    center_ps = soup.find_all("p", align="center")
    titulo = center_ps[0].text.strip() if len(center_ps) > 0 else None
    fecha = center_ps[1].text.strip() if len(center_ps) > 1 else None

    # --- Extraer información del panel (categoría, arma, género, tipo) ---
    panel_body = soup.find("div", class_="panel-body")
    if not panel_body:
        print(f"⚠️ No se encontró panel-body en {url}")
        continue

    info = {
        "Categoria": None,
        "Arma": None,
        "Genero": None,
        "Tipo": None
    }

    for div in panel_body.find_all("div", class_="col-xs-3"):
        strong_tag = div.find("strong")
        if strong_tag:
            key = strong_tag.text.strip().rstrip(":")
            if key in info:
                value = strong_tag.next_sibling.strip() if strong_tag.next_sibling else None
                info[key] = value

    # --- Filtro: solo procesar si Categoria = MAYORES y Tipo = INDIVIDUAL ---
    if info["Categoria"] != "MAYORES" or info["Tipo"] != "INDIVIDUAL":
        print(f"⏭️ Saltando {url} (Categoria={info['Categoria']}, Tipo={info['Tipo']})")
        continue

    # --- Extraer primera tabla ---
    table = soup.find("table")
    if table is None:
        print(f"⚠️ No se encontró tabla en {url}")
        continue

    df = pd.read_html(str(table))[0]

    # --- Agregar columnas con metadatos ---
    df["prueba_id"] = prueba_id
    df["Titulo"] = titulo
    df["Fecha"] = fecha
    df["Categoria"] = info["Categoria"]
    df["Arma"] = info["Arma"]
    df["Genero"] = info["Genero"]
    df["Tipo"] = info["Tipo"]

    all_tables.append(df)
    print(f"✅ Tabla agregada de {url}")
    time.sleep(1)

# --- Unir todas las tablas ---
if all_tables:
    resultados = pd.concat(all_tables, ignore_index=True)
    resultados.to_csv(r"C:\Users\nikol\Documents\Personal\Practicas analisis datos\Proyecto analisis de datos Esgrima\resultados_fedesgrima.csv", index=False, encoding="utf-8-sig")
    print("✅ Datos y tablas extraídos correctamente.")
else:
    print("⚠️ No se encontraron tablas en el rango indicado.")
