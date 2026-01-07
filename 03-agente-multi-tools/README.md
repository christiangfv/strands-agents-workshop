# Nivel 3: Agente Multi-Herramientas

Este nivel introduce el concepto de múltiples herramientas especializadas:

## ¿Qué hace este agente?

- ✅ Modelo LiteLLM configurado
- ✅ **5 herramientas diferentes**:
  - `buscar_clima()`: Consulta clima de ciudades
  - `calcular()`: Operaciones matemáticas
  - `buscar_pokemon()`: Información de Pokémon
  - `contar_chiste()`: Chistes aleatorios
  - `traducir_texto()`: Traducción de idiomas
- ✅ Logger personalizado
- ✅ Sin planner-executor (todavía)

## Cómo ejecutarlo:

```bash
cd 03-agente-multi-tools
python agent.py
```

## Conceptos aprendidos:

- Crear múltiples herramientas especializadas
- Integración con diferentes APIs
- Manejo de errores en herramientas
- Organización de código con múltiples funciones
- Uso de variables de entorno para API keys

## APIs utilizadas:

- OpenWeatherMap (requiere API key)
- PokeAPI (gratuita)
- Official Joke API (gratuita)
- LibreTranslate (gratuita)

## Próximo nivel:

En el [nivel 4](../04-agente-planner-executor/) agregaremos el sistema de planner-executor para tareas complejas.
