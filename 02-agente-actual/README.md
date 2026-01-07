# Nivel 2: Agente Actual Complejo

Este es el agente que teníamos originalmente. Incluye funcionalidades avanzadas:

## ¿Qué hace este agente?

- ✅ Modelo LiteLLM configurado
- ✅ Una herramienta (tool) para datos random
- ✅ Sistema de planner-executor para rutinas de humor
- ✅ Logger personalizado para mostrar el proceso
- ✅ Interfaz de chat interactiva

## Herramientas disponibles:

- `dato_random()`: Obtiene chistes, fotos de mascotas, pokemon, o trivia de APIs públicas

## Cómo ejecutarlo:

```bash
cd 02-agente-actual
python agent.py
```

## Conceptos aprendidos:

- Crear y usar herramientas (tools)
- Sistema de planner-executor
- Callbacks y logging
- Integración con APIs externas
- Manejo de JSON en responses

## Próximo nivel:

En el [nivel 3](../03-agente-multi-tools/) agregaremos más herramientas especializadas.
