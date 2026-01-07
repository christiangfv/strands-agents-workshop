import os
import httpx
import requests
import math
from strands import tool


@tool
def buscar_clima(ciudad: str) -> str:
    """Obtiene el clima actual de una ciudad usando OpenWeatherMap."""
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "❌ OPENWEATHER_API_KEY no configurada"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    print(f"   📡 GET {url}")
    try:
        r = httpx.get(url).json()
        if r.get("cod") == 200:
            temp = r["main"]["temp"]
            desc = r["weather"][0]["description"]
            return f"🌤️ Clima en {ciudad.title()}: {temp}°C, {desc}"
        else:
            return f"❌ Ciudad '{ciudad}' no encontrada"
    except Exception as e:
        return f"❌ Error obteniendo clima: {str(e)}"


@tool
def calcular(operacion: str) -> str:
    """Realiza cálculos matemáticos básicos. Ejemplos: '2 + 3', 'sqrt(16)', 'sin(45)'."""
    try:
        # Evaluar expresiones matemáticas de forma segura
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        allowed_names.update({"__builtins__": {}})

        result = eval(operacion, allowed_names)
        return f"🧮 {operacion} = {result}"
    except Exception as e:
        return f"❌ Error en cálculo '{operacion}': {str(e)}"


@tool
def buscar_pokemon(nombre: str) -> str:
    """Busca información de un Pokémon específico."""
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
        print(f"   📡 GET {url}")
        r = requests.get(url)
        if r.status_code == 404:
            return f"❌ Pokémon '{nombre}' no encontrado"

        data = r.json()
        nombre_pkm = data["name"].title()
        tipos = ", ".join(t["type"]["name"].title() for t in data["types"])
        altura = data["height"] / 10  # convertir a metros
        peso = data["weight"] / 10    # convertir a kg

        return f"🐾 {nombre_pkm} - Tipo: {tipos} - Altura: {altura}m - Peso: {peso}kg"
    except Exception as e:
        return f"❌ Error buscando Pokémon: {str(e)}"


@tool
def contar_chiste() -> str:
    """Cuenta un chiste aleatorio."""
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        print(f"   📡 GET {url}")
        r = httpx.get(url).json()
        return f"😄 {r['setup']} - {r['punchline']}"
    except Exception as e:
        return f"❌ Error obteniendo chiste: {str(e)}"


@tool
def traducir_texto(texto: str, idioma_destino: str = "es") -> str:
    """Traduce texto a otro idioma usando LibreTranslate (sin API key requerida)."""
    try:
        url = "https://libretranslate.com/translate"
        data = {
            "q": texto,
            "source": "auto",
            "target": idioma_destino,
            "format": "text"
        }
        print(f"   📡 POST {url}")
        r = httpx.post(url, json=data).json()
        return f"🌐 Traducción: {r.get('translatedText', 'Error en traducción')}"
    except Exception as e:
        return f"❌ Error traduciendo: {str(e)}"
