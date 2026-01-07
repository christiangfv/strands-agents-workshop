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
from .tools import buscar_clima, calcular, buscar_pokemon, contar_chiste, traducir_texto


# === MODEL ===

def create_model():
    return LiteLLMModel(
        client_args={
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "api_base": "https://openrouter.ai/api/v1",
        },
        model_id="openrouter/google/gemini-2.5-flash",
    )


# === MAIN AGENT ===

SYSTEM_PROMPT = """Eres un asistente multifuncional con acceso a varias herramientas.

Herramientas disponibles:
- buscar_clima(ciudad): Obtiene el clima actual
- calcular(operacion): Realiza cálculos matemáticos
- buscar_pokemon(nombre): Busca info de Pokémon
- contar_chiste(): Cuenta un chiste aleatorio
- traducir_texto(texto, idioma): Traduce texto

Usa las herramientas cuando sea apropiado. Responde siempre en español."""

agent = Agent(
    model=create_model(),
    tools=[buscar_clima, calcular, buscar_pokemon, contar_chiste, traducir_texto],
    system_prompt=SYSTEM_PROMPT,
    callback_handler=logger,
)

print("🛠️  Agente Multi-Herramientas")
print("   Herramientas: clima, calculadora, pokemon, chistes, traductor")
print("   Escribe 'salir' para terminar\n")

while (prompt := input("\nTu: ").strip()) not in ("salir", "exit"):
    if not prompt:
        continue

    agent(prompt)
