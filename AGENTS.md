# AGENTS.md

## Build & Test Commands
```bash
source .venv/bin/activate        # Activate virtual environment
pip install -e ".[dev]"          # Install with dev dependencies
pytest                           # Run all tests
pytest tests/test_file.py::test_name -v  # Run single test
ruff check .                     # Lint code
ruff format .                    # Format code
uvicorn app.main:app --reload    # Run dev server
```

## Code Style Guidelines
- **Types**: Use type hints on all functions and method signatures
- **Imports**: Standard library first, then third-party, then local; use absolute imports
- **Naming**: snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- **Models**: Use Pydantic BaseModel for data validation and serialization
- **Async**: Prefer async/await for I/O operations (Starlette is async-native)
- **Config**: Use pydantic-settings and .env files for configuration
- **Errors**: Raise specific exceptions; use try/except only when handling is needed
- **Docstrings**: Use Google-style docstrings for public functions and classes
