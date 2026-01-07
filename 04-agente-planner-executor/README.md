# Nivel 4: Agente con Planner-Executor Avanzado

Este es el nivel más avanzado del taller. Combina múltiples herramientas con un sistema de planificación inteligente:

## ¿Qué hace este agente?

- ✅ Modelo LiteLLM configurado
- ✅ **5 herramientas especializadas**:
  - `buscar_clima()`: Consulta clima
  - `calcular()`: Operaciones matemáticas
  - `buscar_pokemon()`: Info de Pokémon
  - `contar_chiste()`: Chistes aleatorios
  - `traducir_texto()`: Traducción
- ✅ **Sistema de Planner-Executor**:
  - Planner: Crea planes JSON detallados
  - Executor: Ejecuta planes paso a paso
- ✅ Comando especial `plan [tarea]` para planificación
- ✅ Logger personalizado

## Cómo ejecutarlo:

```bash
cd 04-agente-planner-executor
python agent.py
```

## Conceptos aprendidos:

- Arquitectura planner-executor
- Planes JSON estructurados
- Ejecución secuencial de tareas
- Múltiples herramientas coordinadas
- Comandos especiales del agente
- Manejo de contexto en conversaciones complejas

## APIs utilizadas:

- OpenWeatherMap (requiere API key)
- PokeAPI (gratuita)
- Official Joke API (gratuita)
- LibreTranslate (gratuita)

## Ejemplos de uso:

```
Tu: plan organizar una fiesta pokemon
Tu: calcula 2**10 y busca el clima en Tokyo
Tu: traduce "Hello world" al frances y cuentame un chiste
```

## Este es el nivel final del taller

¡Felicitaciones! Has completado todos los niveles del taller de strands agents. Ahora tienes experiencia con:

1. ✅ Agentes básicos
2. ✅ Agentes con herramientas
3. ✅ Múltiples herramientas especializadas
4. ✅ Arquitecturas planner-executor avanzadas
