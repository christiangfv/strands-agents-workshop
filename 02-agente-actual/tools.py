import os
import json
import httpx
import random
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel


def create_model():
    return LiteLLMModel(
        client_args={
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "api_base": "https://openrouter.ai/api/v1",
        },
        model_id="openrouter/google/gemini-2.5-flash",
    )


def logger(**kwargs):
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


PLANNER_PROMPT = """Eres un planificador de rutinas de humor. Tu trabajo es crear un plan detallado
para entretener al usuario. Dado un tema o solicitud, genera un plan JSON con pasos secuenciales.

Responde SOLO con JSON valido en este formato:
{
  "tema": "descripcion del tema",
  "pasos": [
    {"id": 1, "tipo": "chiste|trivia|pokemon|gato|perro|comentario", "instruccion": "que hacer"},
    ...
  ]
}

Tipos disponibles:
- chiste: contar un chiste de la API
- trivia: hacer una pregunta de trivia
- pokemon: mostrar un pokemon random
- gato/perro: mostrar foto de mascota
- comentario: tu propio comentario gracioso (no usa API)

Crea rutinas de 3-5 pasos que fluyan bien y sean entretenidas."""

EXECUTOR_PROMPT = """Eres un comediante ejecutando una rutina de humor paso a paso.
Tienes acceso a la tool dato_random para obtener contenido.
Ejecuta cada paso con entusiasmo y agrega tu toque personal.
Responde en español con emojis."""


@tool
def dato_random(tipo: str = "chiste") -> str:
    """Obtiene datos random de internet: chiste, gato, perro, pokemon, o trivia."""
    apis = {
        "chiste": "https://official-joke-api.appspot.com/random_joke",
        "gato": "https://api.thecatapi.com/v1/images/search",
        "perro": "https://dog.ceo/api/breeds/image/random",
        "pokemon": f"https://pokeapi.co/api/v2/pokemon/{random.randint(1, 151)}",
        "trivia": "https://opentdb.com/api.php?amount=1",
    }
    url = apis.get(tipo, apis["chiste"])
    print(f"   📡 GET {url}")
    r = httpx.get(url).json()
    if tipo == "chiste":
        return f"{r['setup']} - {r['punchline']}"
    if tipo == "gato":
        return f"Foto de gato: {r[0]['url']}"
    if tipo == "perro":
        return f"Foto de perro: {r['message']}"
    if tipo == "pokemon":
        return f"Pokemon: {r['name'].title()}, Tipo: {', '.join(t['type']['name'] for t in r['types'])}"
    if tipo == "trivia":
        q = r["results"][0]
        return f"Trivia ({q['category']}): {q['question']} Respuesta: {q['correct_answer']}"
    return f"{r['setup']} - {r['punchline']}"


@tool
def ejecutar_rutina(plan_json: str) -> str:
    """Ejecuta una rutina de humor dado un plan JSON. El plan debe tener 'pasos' con 'tipo' e 'instruccion'."""
    print("\n🎭 === EJECUTANDO RUTINA ===\n")

    plan = json.loads(plan_json)
    executor = Agent(
        model=create_model(),
        tools=[dato_random],
        system_prompt=EXECUTOR_PROMPT,
        callback_handler=logger,
    )

    resultados = []
    for i, paso in enumerate(plan.get("pasos", []), 1):
        print(f"\n📍 Paso {i}/{len(plan['pasos'])}: {paso.get('tipo', 'comentario')}")
        print("-" * 40)

        if paso["tipo"] == "comentario":
            prompt = f"Haz un comentario gracioso sobre: {paso['instruccion']}"
        else:
            prompt = f"Usa dato_random con tipo='{paso['tipo']}' y luego {paso['instruccion']}"

        resultado = executor(prompt)
        resultados.append(f"Paso {i}: {resultado}")

    print("\n🎭 === FIN DE RUTINA ===\n")
    return "\n".join(resultados)
