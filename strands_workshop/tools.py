"""Herramientas comunes para agentes del taller."""

from typing import List
from strands import tool


@tool
def echo_tool(message: str) -> str:
    """Herramienta simple que repite el mensaje (para testing).

    Args:
        message: El mensaje a repetir.

    Returns:
        El mensaje repetido.
    """
    return f"Echo: {message}"


@tool
def count_words(text: str) -> int:
    """Cuenta las palabras en un texto.

    Args:
        text: El texto a analizar.

    Returns:
        Número de palabras.
    """
    words = text.split()
    return len(words)


@tool
def reverse_text(text: str) -> str:
    """Invierte el orden de los caracteres en un texto.

    Args:
        text: El texto a invertir.

    Returns:
        El texto invertido.
    """
    return text[::-1]


# Lista de herramientas básicas disponibles
BASIC_TOOLS = [echo_tool, count_words, reverse_text]

# Lista de todas las herramientas disponibles en el taller
ALL_TOOLS = BASIC_TOOLS
