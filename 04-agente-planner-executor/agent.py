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


# === HERRAMIENTAS ===
from .tools import buscar_clima, calcular, buscar_pokemon, contar_chiste, traducir_texto, ejecutar_plan

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

PLANNER_PROMPT = """Eres un planificador inteligente. Tu trabajo es crear planes detallados paso a paso
para completar tareas complejas usando las herramientas disponibles.

Herramientas disponibles:
- buscar_clima(ciudad): clima actual
- calcular(operacion): cálculos matemáticos
- buscar_pokemon(nombre): info de Pokémon
- contar_chiste(): chiste aleatorio
- traducir_texto(texto, idioma): traducción

Responde SOLO con JSON valido en este formato:
{
  "objetivo": "descripcion del objetivo principal",
  "pasos": [
    {"id": 1, "herramienta": "nombre_herramienta", "parametros": {"param1": "valor1"}, "explicacion": "por que este paso"},
    {"id": 2, "tipo": "comentario", "contenido": "texto a decir", "explicacion": "comentario del agente"},
    ...
  ]
}

Crea planes de 3-6 pasos que sean lógicos y útiles."""

EXECUTOR_PROMPT = """Eres un ejecutor inteligente que sigue planes paso a paso.
Tienes acceso a múltiples herramientas y puedes ejecutar cada paso del plan.
Sé detallado en tus explicaciones y mantén el contexto de la conversación.
Responde siempre en español con emojis apropiados."""



# === MAIN AGENT ===

SYSTEM_PROMPT = """Eres un asistente avanzado con múltiples herramientas y capacidad de planificación.

Para tareas simples: usa las herramientas directamente.
Para tareas complejas: crea un plan detallado y ejecutalo.

Herramientas disponibles:
- buscar_clima(ciudad)
- calcular(operacion)
- buscar_pokemon(nombre)
- contar_chiste()
- traducir_texto(texto, idioma)

Comandos especiales:
- "plan [tarea]": crea y ejecuta un plan para esa tarea
- "ayuda": muestra esta información

Responde siempre en español."""

planner = Agent(
    model=create_model(),
    system_prompt=PLANNER_PROMPT,
    callback_handler=None,  # silencioso
)

main_agent = Agent(
    model=create_model(),
    tools=[buscar_clima, calcular, buscar_pokemon, contar_chiste, traducir_texto, ejecutar_plan],
    system_prompt=SYSTEM_PROMPT,
    callback_handler=logger,
)

print("🚀 Agente Avanzado con Planner-Executor")
print("   Herramientas: clima, calculadora, pokemon, chistes, traductor, planes")
print("   Comandos: 'plan [tarea]' para planificación avanzada")
print("   Escribe 'salir' para terminar\n")

while (prompt := input("\nTu: ").strip()) not in ("salir", "exit"):
    if not prompt:
        continue

    # Comando especial para planificación
    if prompt.lower().startswith("plan "):
        tarea = prompt[5:].strip()
        print(f"\n📋 Planificando: {tarea}")
        plan_response = planner(f"Crea un plan detallado para: {tarea}")
        plan_text = str(plan_response)

        if "{" in plan_text:
            plan_json = plan_text[plan_text.find("{") : plan_text.rfind("}") + 1]
            print(f"📋 Plan creado: {plan_json[:100]}...")
            main_agent(f"Ejecuta este plan: {plan_json}")
        else:
            print("❌ Error creando plan")
            main_agent(prompt)
    else:
        main_agent(prompt)
