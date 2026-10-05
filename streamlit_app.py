# Diagnostic : charge les modules un par un et affiche l'étape atteinte.
import sys
import time

import streamlit as st

st.title("Diagnostic de démarrage")
st.write(f"Python {sys.version.split()[0]} · Streamlit {st.__version__}")

steps = [
    ("pandas", "import pandas"),
    ("folium", "import folium"),
    ("streamlit_folium", "from streamlit_folium import st_folium"),
    ("ee", "import ee"),
    ("shapely", "import shapely"),
    ("pyproj", "import pyproj"),
    ("utils.vector_io", "import utils.vector_io"),
    ("utils.geometry", "import utils.geometry"),
    ("utils.ndvi_processing", "import utils.ndvi_processing"),
    ("utils.gee_ndvi", "import utils.gee_ndvi"),
]
for name, stmt in steps:
    t0 = time.time()
    try:
        exec(stmt)
        st.write(f"✅ {name} ({time.time() - t0:.1f} s)")
    except Exception as e:
        st.error(f"❌ {name} : {type(e).__name__} — {e}")

t0 = time.time()
try:
    from utils.gee_ndvi import init_gee
    init_gee(st.secrets["GEE_SERVICE_ACCOUNT"], st.secrets["GEE_PRIVATE_KEY"])
    st.write(f"✅ Connexion Earth Engine ({time.time() - t0:.1f} s)")
except Exception as e:
    st.error(f"❌ Connexion Earth Engine : {type(e).__name__} — {e}")

st.success("Diagnostic terminé")
