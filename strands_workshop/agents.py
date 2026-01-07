"""Módulo de agentes para el taller de Strands."""

from typing import Optional, List
from strands import Agent
from strands.models.litellm import LiteLLMModel


def create_basic_agent(system_prompt: str = "Eres un asistente amigable.") -> Agent:
    """Crea un agente básico con configuración estándar.

    Args:
        system_prompt: El prompt del sistema para el agente.

    Returns:
        Un agente configurado con modelo LiteLLM.
    """
    model = LiteLLMModel(
        client_args={
            "api_key": "your-api-key-here",  # Debe ser configurado externamente
            "api_base": "https://openrouter.ai/api/v1",
        },
        model_id="openrouter/google/gemini-2.5-flash",
    )

    return Agent(model=model, system_prompt=system_prompt)


def create_agent_with_tools(
    system_prompt: str,
    tools: List,
    model_config: Optional[dict] = None
) -> Agent:
    """Crea un agente con herramientas.

    Args:
        system_prompt: El prompt del sistema.
        tools: Lista de herramientas (funciones decoradas con @tool).
        model_config: Configuración opcional del modelo.

    Returns:
        Un agente con herramientas configuradas.
    """
    if model_config is None:
        model_config = {
            "api_key": "your-api-key-here",
            "api_base": "https://openrouter.ai/api/v1",
        }

    model = LiteLLMModel(
        client_args=model_config,
        model_id="openrouter/google/gemini-2.5-flash",
    )

    return Agent(
        model=model,
        tools=tools,
        system_prompt=system_prompt,
    )
