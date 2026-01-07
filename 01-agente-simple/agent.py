import os
from dotenv import load_dotenv
from strands import Agent
from strands.models.litellm import LiteLLMModel
import litellm

load_dotenv()
litellm.suppress_debug_info = True

def create_model():
    """Crear modelo LiteLLM básico"""
    return LiteLLMModel(
        client_args={
            "api_key": os.getenv("OPENROUTER_API_KEY"),
            "api_base": "https://openrouter.ai/api/v1",
        },
        model_id="openrouter/google/gemini-2.5-flash",
    )

# Crear agente ultra simple
agent = Agent(
    model=create_model(),
    system_prompt="Eres un asistente amigable. Responde de manera concisa y útil.",
)

print("🤖 Agente Ultra Simple")
print("Escribe 'salir' para terminar\n")

while (prompt := input("Tu: ").strip()) not in ("salir", "exit"):
    if not prompt:
        continue

    respuesta = agent(prompt)
    print(f"Agente: {respuesta}")
