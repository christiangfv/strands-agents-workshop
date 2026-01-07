import os
import json
import httpx
import requests
import math
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel


def create_model():
    """Función auxiliar para crear el modelo (importada desde agent.py)"""
    return LiteLLMModel(
        client_args={
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "api_base": "https://openrouter.ai/api/v1",
        },
        model_id="openrouter/google/gemini-2.5-flash",
    )


def logger(**kwargs):
    """Función de logging (importada desde agent.py)"""
    if kwargs.get("init_event_loop"):
        print("🔄 Iniciando...")
    elif kwargs.get("start_event_loop"):
        print("▶️  Pensando...")
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        t = kwargs["current_tool_use"]
        print(f"🔧 Tool: {t['name']}({t.get('input', {})})")
    elif "data" in kwargs:
        print(kwargs["data"], end="", flush=True)
    elif kwargs.get("complete"):
        print("\n✅ Listo")


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
        r = httpx.get(url).json()
        if "error" in r:
            return f"❌ Pokémon '{nombre}' no encontrado"

        nombre_pkm = r["name"].title()
        tipos = ", ".join(t["type"]["name"].title() for t in r["types"])
        altura = r["height"] / 10  # convertir a metros
        peso = r["weight"] / 10    # convertir a kg

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
    """Traduce texto a otro idioma usando LibreTranslate."""
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


@tool
def ejecutar_plan(plan_json: str) -> str:
    """Ejecuta un plan detallado paso a paso usando las herramientas disponibles."""
    print("\n🎯 === EJECUTANDO PLAN ===\n")

    plan = json.loads(plan_json)
    executor = Agent(
        model=create_model(),
        tools=[buscar_clima, calcular, buscar_pokemon, contar_chiste, traducir_texto],
        system_prompt="""Eres un ejecutor inteligente que sigue planes paso a paso.
Tienes acceso a múltiples herramientas y puedes ejecutar cada paso del plan.
Sé detallado en tus explicaciones y mantén el contexto de la conversación.
Responde siempre en español con emojis apropiados.""",
        callback_handler=logger,
    )

    resultados = []
    for i, paso in enumerate(plan.get("pasos", []), 1):
        print(f"\n📍 Paso {i}/{len(plan['pasos'])}: {paso.get('herramienta', 'comentario')}")
        print("-" * 50)

        if paso.get("tipo") == "comentario":
            # Paso de comentario - el executor lo maneja directamente
            prompt = f"Comentario: {paso['contenido']}"
        elif paso.get("herramienta"):
            # Usar herramienta específica
            tool_name = paso["herramienta"]
            params = paso.get("parametros", {})
            params_str = ", ".join(f"{k}='{v}'" for k, v in params.items())
            prompt = f"Usa la herramienta {tool_name}({params_str}) para: {paso.get('explicacion', '')}"
        else:
            prompt = f"Ejecuta: {paso}"

        resultado = executor(prompt)
        resultados.append(f"Paso {i}: {resultado}")

    print("\n🎯 === FIN DEL PLAN ===\n")
    return "\n".join(resultados)
