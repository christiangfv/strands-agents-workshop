# 🤖 Strands Agents Workshop

<div align="center">

![Strands Agents Workshop](https://img.shields.io/badge/Strands-Agents-blue?style=for-the-badge&logo=robot)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

*Un taller progresivo para dominar agentes inteligentes con Strands*

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?style=flat&logo=github)](https://github.com/christianfuentesradar/strands-agents-workshop)
[![CI](https://github.com/christianfuentesradar/strands-agents-workshop/actions/workflows/ci.yml/badge.svg)](https://github.com/christianfuentesradar/strands-agents-workshop/actions)
[![Python Versions](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)](https://www.python.org/)

[🚀 Inicio Rápido](#-instalación) • [📚 Documentación](#-estructura-del-taller) • [🤝 Contribuir](CONTRIBUTING.md) • [📜 Código de Conducta](CODE_OF_CONDUCT.md) • [⚙️ GitHub Setup](GITHUB_SETUP.md)

</div>

---

## 🌟 ¿Qué es este taller?

**Strands Agents Workshop** es un curso práctico diseñado para enseñarte a construir agentes inteligentes usando el framework [Strands](https://strands.ai/). Desde lo más básico hasta arquitecturas complejas, aprenderás paso a paso cómo crear agentes capaces de razonar, usar herramientas y planificar tareas.

### 🎯 ¿Para quién es?

- 👨‍💻 **Desarrolladores** que quieren aprender sobre agentes IA
- 🎓 **Estudiantes** de IA/ML interesados en agentes conversacionales
- 🏗️ **Arquitectos** que necesitan entender patrones de agentes
- 🤖 **Entusiastas** de IA que quieren experimentar con LLMs

### 📈 Nivel de Dificultad

🟢 **Principiante** → 🟡 **Intermedio** → 🟠 **Avanzado** → 🔴 **Experto**

---

## 📚 Estructura del Taller

### 🟢 [01-agente-simple](./01-agente-simple/)
**Fundamentos Básicos**
- ✅ Agente conversacional simple
- ✅ Integración con LiteLLM
- ✅ Sin herramientas ni complejidad
- 🎯 **Aprendizaje**: API básica de Strands

```bash
cd 01-agente-simple && python agent.py
```

### 🟡 [02-agente-actual](./02-agente-actual/)
**Primeras Herramientas**
- ✅ Una herramienta funcional (datos random)
- ✅ Sistema planner-executor básico
- ✅ Logging personalizado
- 🎯 **Aprendizaje**: Patrón tool + planificación

```bash
cd 02-agente-actual && python agent.py
```

### 🟠 [03-agente-multi-tools](./03-agente-multi-tools/)
**Arquitectura Multi-Herramienta**
- ✅ **5 herramientas especializadas**:
  - 🌤️ Consulta de clima
  - 🔢 Calculadora matemática
  - 🐾 Información de Pokémon
  - 😄 Generador de chistes
  - 🌐 Traductor de idiomas
- ✅ Integración con APIs externas
- 🎯 **Aprendizaje**: Arquitectura modular

```bash
cd 03-agente-multi-tools && python agent.py
```

### 🔴 [04-agente-planner-executor](./04-agente-planner-executor/)
**Agente Avanzado Completo**
- ✅ Todas las herramientas del nivel 3
- ✅ **Sistema planner-executor inteligente**
- ✅ Planes JSON estructurados
- ✅ Comando `plan [tarea]` para tareas complejas
- 🎯 **Aprendizaje**: Coordinación y planificación avanzada

```bash
cd 04-agente-planner-executor && python agent.py
```

---

## 🚀 Instalación

### Prerrequisitos

- **Python 3.8+**
- **Git**
- **API Key de OpenRouter** (gratuita)

### Instalación Rápida

```bash
# 1. Clona el repositorio
git clone https://github.com/christiangfv/strands-agents-workshop.git
cd strands-agents-workshop

# 2. Crea entorno virtual
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Instala dependencias
pip install -e ".[dev]"

# 4. Configura variables de entorno
cp .env.example .env
# Edita .env con tu OPENROUTER_API_KEY
```

### Verificación

```bash
# Ejecuta tests
pytest

# Verifica instalación
python -c "import strands; print('✅ Strands instalado correctamente')"
```

---

## 🎮 Uso Interactivo

### Nivel 1 - Básico
```bash
cd 01-agente-simple
python agent.py
```
```
Tu: Hola, ¿cómo estás?
Agente: ¡Hola! Estoy bien, gracias por preguntar. ¿En qué puedo ayudarte?
```

### Nivel 3 - Multi-herramientas
```bash
cd 03-agente-multi-tools
python agent.py
```
```
Tu: ¿Qué tiempo hace en Madrid?
Agente: 🌤️ Clima en Madrid: 22°C, cielo despejado

Tu: Calcula 2 elevado a la potencia 10
Agente: 🧮 2**10 = 1024.0
```

### Nivel 4 - Planificación Avanzada
```bash
cd 04-agente-planner-executor
python agent.py
```
```
Tu: plan organizar una fiesta pokemon
Agente: 📋 Planificando: organizar una fiesta pokemon
📋 Plan creado: {"objetivo": "organizar fiesta pokemon", "pasos": [...]}
🎯 === EJECUTANDO PLAN ===
📍 Paso 1/4: Buscar información de Pokémon aleatorios
🐾 Pikachu - Tipo: Eléctrico - Altura: 0.4m - Peso: 6.0kg
...
```

---

## 🏗️ Arquitectura

```
strands-agents-workshop/
├── 01-agente-simple/          # 🟢 Fundamentos
│   └── agent.py               # Agente básico
├── 02-agente-actual/          # 🟡 Tools básicas
│   ├── agent.py               # Lógica principal
│   └── tools.py               # Herramientas
├── 03-agente-multi-tools/     # 🟠 Multi-tools
│   ├── agent.py               # Lógica principal
│   └── tools.py               # 5 herramientas
├── 04-agente-planner-executor/# 🔴 Avanzado
│   ├── agent.py               # Lógica principal
│   └── tools.py               # Tools + planner
├── tests/                     # 🧪 Tests
├── docs/                      # 📖 Documentación
├── pyproject.toml             # ⚙️ Configuración moderna
├── requirements.txt           # 📦 Dependencias
└── README.md                  # 📚 Este archivo
```

### Principios de Diseño

- 🎯 **Progresión lógica**: Cada nivel construye sobre el anterior
- 🔧 **Separación de responsabilidades**: Tools separadas de lógica de agentes
- 🧪 **Tests incluidos**: Cobertura de funcionalidad crítica
- 📚 **Documentación completa**: README en cada nivel
- 🚀 **Production-ready**: Configuración moderna con pyproject.toml

---

## 🧪 Testing

```bash
# Ejecutar toda la suite de tests
pytest

# Tests con cobertura
pytest --cov=strands_workshop --cov-report=html

# Tests de un nivel específico
pytest tests/test_01_agente_simple/

# Tests de integración
pytest tests/test_integration/
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Lee nuestra [Guía de Contribución](CONTRIBUTING.md) para:

- 🐛 Reportar bugs
- 💡 Sugerir nuevas features
- 📝 Mejorar documentación
- 🛠️ Contribuir código
- 🧪 Agregar tests

### Flujo de Trabajo

1. Fork el proyecto
2. Crea una feature branch: `git checkout -b feature/nueva-funcionalidad`
3. Commit tus cambios: `git commit -m 'feat: agrega nueva funcionalidad'`
4. Push a la branch: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

- **[Strands](https://strands.ai/)** por el framework de agentes
- **[OpenRouter](https://openrouter.ai/)** por acceso a modelos de IA
- **Comunidad Open Source** por las inspiraciones y mejores prácticas

---

## 📞 Contacto

**Christian GFV**
- 📧 Email: christiangfv@gmail.com
- 🔗 GitHub: [@christiangfv](https://github.com/christiangfv)
- 🐛 Issues: [GitHub Issues](https://github.com/christiangfv/strands-agents-workshop/issues)

---

<div align="center">

**⭐ Si te gusta el proyecto, dale una estrella en GitHub!**

*Hecho con ❤️ para la comunidad de IA*

</div>
