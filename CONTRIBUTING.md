# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al **Taller de Strands Agents**! Este documento describe las pautas para contribuir al proyecto.

## 📋 Código de Conducta

Este proyecto sigue un código de conducta para asegurar que la comunidad sea acogedora para todos. Al participar, aceptas:

- Ser respetuoso con todos los participantes
- Usar lenguaje inclusivo
- Aceptar responsabilidad constructiva
- Mostrar empatía hacia otros puntos de vista
- Ayudar a mantener la comunidad positiva

## 🚀 Cómo Contribuir

### Tipos de Contribuciones

- 🐛 **Reportar bugs**: Usa los [issues de GitHub](https://github.com/christiangfv/strands-agents-workshop/issues)
- 💡 **Sugerir mejoras**: Crea un issue con la etiqueta `enhancement`
- 📝 **Mejorar documentación**: Edita READMEs, agrega ejemplos, etc.
- 🛠️ **Contribuir código**: Implementa nuevas features o arregla bugs
- 🧪 **Agregar tests**: Mejora la cobertura de tests

### Proceso de Contribución

1. **Fork** el repositorio
2. **Crea una branch** para tu feature: `git checkout -b feature/nueva-funcionalidad`
3. **Haz tus cambios** siguiendo las guías de estilo
4. **Agrega tests** si corresponde
5. **Ejecuta los tests**: `pytest`
6. **Formatea el código**: `ruff format .`
7. **Verifica linting**: `ruff check .`
8. **Commit** con mensajes descriptivos
9. **Push** a tu fork
10. **Crea un Pull Request**

## 🛠️ Configuración del Entorno de Desarrollo

### Prerrequisitos

- Python 3.8+
- Git
- API keys para servicios externos (opcional para desarrollo básico)

### Instalación

```bash
# Clona el repositorio
git clone https://github.com/christiangfv/strands-agents-workshop.git
cd strands-agents-workshop

# Crea entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instala dependencias
pip install -e ".[dev]"

# Configura variables de entorno
cp .env.example .env
# Edita .env con tus API keys
```

### Comandos de Desarrollo

```bash
# Ejecutar tests
pytest

# Verificar cobertura
pytest --cov=strands_workshop

# Formatear código
ruff format .

# Verificar estilo
ruff check .

# Ejecutar mypy
mypy .

# Ejecutar todo junto
tox  # si tienes tox instalado
```

## 📝 Guías de Estilo

### Python

- Seguimos [PEP 8](https://pep8.org/)
- Usamos [Ruff](https://github.com/charliermarsh/ruff) para linting y formateo
- Usamos [MyPy](https://mypy-lang.org/) para type checking
- Longitud máxima de línea: 88 caracteres

### Commits

Usamos [Conventional Commits](https://conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Tipos comunes:
- `feat`: Nueva funcionalidad
- `fix`: Arreglo de bug
- `docs`: Cambios en documentación
- `style`: Cambios de estilo (formateo, etc.)
- `refactor`: Refactorización de código
- `test`: Agregar o modificar tests
- `chore`: Cambios de mantenimiento

Ejemplos:
```
feat: agregar nueva herramienta de cálculo
fix: corregir error en API de clima
docs: actualizar README del nivel 3
```

### Branches

- `main`: Branch principal, solo releases estables
- `develop`: Branch de desarrollo
- `feature/nombre`: Nuevas funcionalidades
- `bugfix/nombre`: Arreglos de bugs
- `hotfix/nombre`: Arreglos críticos

## 🧪 Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Tests específicos
pytest tests/test_agente.py

# Con cobertura
pytest --cov=strands_workshop --cov-report=html

# Tests de un nivel específico
pytest tests/01-agente-simple/
```

### Escribir Tests

- Los tests van en `tests/` organizado por nivel
- Usa `pytest` como framework
- Nombra archivos: `test_*.py`
- Nombra funciones: `test_*`
- Incluye docstrings descriptivos

Ejemplo:
```python
def test_agente_basico_responde():
    """Test que el agente básico responde a mensajes."""
    agent = create_basic_agent()
    response = agent("Hola")
    assert isinstance(response, str)
    assert len(response) > 0
```

## 📚 Documentación

### READMEs

Cada nivel debe tener un README.md que incluya:
- Descripción del nivel
- Qué conceptos se aprenden
- Cómo ejecutar el código
- Ejemplos de uso

### Docstrings

Usa docstrings en formato Google:

```python
def buscar_clima(ciudad: str) -> str:
    """Obtiene el clima actual de una ciudad.

    Args:
        ciudad: Nombre de la ciudad

    Returns:
        String con información del clima

    Raises:
        ConnectionError: Si no hay conexión a internet
    """
```

## 🔐 Variables de Entorno

Para desarrollo local, crea un archivo `.env` con:

```bash
# API Keys (opcional para desarrollo básico)
OPENROUTER_API_KEY=tu_api_key_aqui
OPENWEATHER_API_KEY=tu_api_key_opcional
```

## 📞 Soporte

- 🐛 **Bugs**: [GitHub Issues](https://github.com/christiangfv/strands-agents-workshop/issues)
- 💬 **Discusiones**: [GitHub Discussions](https://github.com/christiangfv/strands-agents-workshop/discussions)
- 📧 **Email**: christiangfv@gmail.com

## 🙏 Reconocimientos

¡Gracias a todos los contribuidores que hacen posible este proyecto!

---

*Esta guía se basa en mejores prácticas de la comunidad open source.*
