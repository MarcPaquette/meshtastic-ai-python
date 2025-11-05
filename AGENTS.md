## Build/Lint/Test Commands
- Install dependencies: `venv/bin/pip install -r requirements.txt`
- Run all tests: `venv/bin/python -m pytest`
- Run single test: `venv/bin/python -m pytest tests/test_file.py::TestClass::test_method`
- Lint: `venv/bin/python -m flake8 .`
- Format: `venv/bin/python -m black .`

## Architecture
- Language: Python 3.8+
- Key libraries: Ollama for local LLM integration
- Structure: Modular scripts in root, venv for dependencies
- No databases or APIs yet; focused on AI chat functionality
- Meshtastic integration planned for mesh networking

## Code Style Guidelines
- Follow PEP 8 with Black formatting
- Use type hints for all function parameters and return types
- Imports: standard library, then third-party, then local (alphabetized)
- Naming: snake_case for variables/functions, CamelCase for classes
- Error handling: Use try/except with specific exceptions, log errors
- Docstrings: Use Google-style for functions and classes
- Constants: UPPER_CASE
- No rules files found (.cursor, .cursorrules, CLAUDE.md, etc.)
