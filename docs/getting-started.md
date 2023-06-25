## How to use

1. Setup and activate the Python environment of your choice.

```shell
cp .env.example .env
```

2. Run the following command to install the required dependencies:

```shell
pip install poetry
poetry shell
poetry install
```

3. Test the application by running the following command:

```shell
poetry run pytest
```

4. Run the following command to launch FastAPI in development mode:

```shell
poetry run uvicorn app.main:app --reload
```

5. Dockerize the application by running the following command:

```shell
docker-compose up --build
```

### Documentation

The documentation of the API is available at the following URL: http://localhost:8000/api/v1/docs

## File Structure

```shell
# AINewsTracker.svg & AINewsTracker_transparent.svg: Logo or graphic resources
# app: Main application code directory
# ├── config.py: File that contains the configuration settings of the application
# ├── core: Directory that includes essential parts of the application
# ├── ├── database: Includes scripts for managing database connections
# ├── ├── ├── db.py: Main database module containing connection settings, queries, etc.
# ├── ├── logging.py: File that sets up the logging for the application
# ├── ├── repo: Directory that contains scripts for database operations
# ├── ├── services: Contains service functions for different operations
# ├── ├── telemetry: Directory containing scripts for system logging and monitoring
# ├── main.py: Entry point of the application
# ├── models: Directory containing the data models used by the application
# ├── routers: Directory containing FastAPI routers (request handling logic)
# ├── static: Contains static files (images, CSS, JavaScript, etc.)
# ├── __version__.py: File that contains the version number of the application
# CODE_OF_CONDUCT.md: Markdown file outlining the code of conduct for the project
# CONTRIBUTING.md: Markdown file outlining the guidelines for contributing to the project
# deploy: Directory for deployment-related files and scripts
# ├── docker-compose.yml: Docker Compose file for setting up the production environment
# ├── README.md: Markdown file with instructions for deploying the application
# docker-compose.yml: Docker Compose file for setting up the development environment
# Dockerfile: Contains instructions for Docker to build an image for the application
# LICENSE: The license of the project
# monitoring: Contains configuration files for monitoring tools
# poetry.lock & pyproject.toml: Configuration files for Python project and dependency management (Poetry)
# README.md: General project documentation and overview
# renovate.json: Configuration file for Renovate (automates dependency updates)
# requirements-dev.txt & requirements.txt: Python dependencies for development and production environments
# SECURITY.md: Markdown file outlining the security policy of the project
# Test-AI.ipynb: A Jupyter notebook file for testing AI functionalities
# tests: Directory for test modules
# wiki: Directory for additional project documentation or guides

```