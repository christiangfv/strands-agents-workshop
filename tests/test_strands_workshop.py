"""Tests básicos para el paquete strands_workshop."""

import pytest
from strands_workshop import __version__, agents, tools


class TestPackageBasics:
    """Tests básicos del paquete."""

    def test_version(self):
        """Test que la versión está definida."""
        assert __version__ is not None
        assert isinstance(__version__, str)

    def test_imports(self):
        """Test que los módulos se pueden importar."""
        assert agents is not None
        assert tools is not None

    def test_basic_tools_available(self):
        """Test que las herramientas básicas están disponibles."""
        assert len(tools.BASIC_TOOLS) > 0
        assert len(tools.ALL_TOOLS) > 0


class TestAgentCreation:
    """Tests para la creación de agentes."""

    def test_create_basic_agent(self):
        """Test creación de agente básico."""
        # Nota: Este test requiere configuración de API key
        # En un entorno real, usaríamos mocks
        agent = agents.create_basic_agent()
        assert agent is not None
        # Verificar que tenga los atributos básicos
        assert hasattr(agent, 'model')
        assert hasattr(agent, 'system_prompt')


class TestTools:
    """Tests para las herramientas."""

    def test_echo_tool(self):
        """Test herramienta echo."""
        result = tools.echo_tool("test message")
        assert "Echo: test message" in result

    def test_count_words(self):
        """Test contador de palabras."""
        result = tools.count_words("hello world test")
        assert result == 3

    def test_reverse_text(self):
        """Test inversión de texto."""
        result = tools.reverse_text("hello")
        assert result == "olleh"
