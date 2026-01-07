import os
import json
import httpx
import litellm
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.litellm import LiteLLMModel

load_dotenv()
litellm.suppress_debug_info = True


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


# === TOOLS ===


@tool
def dato_random(tipo: str = "chiste") -> str:
    """Obtiene datos random de internet: chiste, gato, perro, pokemon, o trivia."""
    import random

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


# === MODEL ===


def create_model():
    return LiteLLMModel(
        client_args={
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "api_base": "https://openrouter.ai/api/v1",
        },
        model_id="openrouter/google/gemini-2.5-flash",
    )


# === PLANNER-EXECUTOR ===

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


# === MAIN AGENT ===

SYSTEM_PROMPT = """Eres un director de comedia. Cuando el usuario pida entretenimiento o una rutina:
1. Usa tu creatividad para planificar una rutina de humor
2. Genera un plan JSON y pasalo a ejecutar_rutina

Para solicitudes simples (un chiste, un pokemon, etc), usa dato_random directamente.
Para rutinas completas o "entreteneme", crea un plan y ejecutalo.

Responde siempre en español."""

planner = Agent(
    model=create_model(),
    system_prompt=PLANNER_PROMPT,
    callback_handler=None,  # silencioso
)

main_agent = Agent(
    model=create_model(),
    tools=[dato_random, ejecutar_rutina],
    system_prompt=SYSTEM_PROMPT,
    callback_handler=logger,
)

print("🎭 Agente de Humor con Planner-Executor")
print("   Comandos: 'rutina', 'entreteneme', o pide algo específico")
print("   Escribe 'salir' para terminar\n")

while (prompt := input("\nTu: ").strip()) not in ("salir", "exit"):
    if not prompt:
        continue

    # Si pide rutina, primero planificamos
    if any(
        word in prompt.lower()
        for word in ["rutina", "entreteneme", "show", "espectáculo"]
    ):
        print("\n📋 Planificando rutina...")
        plan_response = planner(f"Crea una rutina de humor sobre: {prompt}")
        # Extraer JSON del response
        plan_text = str(plan_response)
        if "{" in plan_text:
            plan_json = plan_text[plan_text.find("{") : plan_text.rfind("}") + 1]
            print(f"📋 Plan: {plan_json[:100]}...")
            main_agent(f"Ejecuta esta rutina: {plan_json}")
        else:
            main_agent(prompt)
    else:
        main_agent(prompt)
