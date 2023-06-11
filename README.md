<p align="center">
    <img width="50%" src="./AINewsTracker_transparent.svg" alt="AINewsTracker"/>
    <h1 align="center">AINewsTracker </h1>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License MIT"/>
    <img src="https://img.shields.io/badge/-FastAPI-009681?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
    <img src="https://img.shields.io/badge/-MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
    <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
    <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy"/>
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
    <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook"/>
    <br>
    <img src=".github/badge/coverage.svg" alt="Coverage" />
</p>

## What is AINewsTracker?

AINewsTracker is a sophisticated web application that backtests the influence of financial news on the stock market. It utilizes artificial intelligence to categorize, filter, and analyze financial news from a variety of trustworthy international and regional sources. This allows users to monitor and predict potential impacts on market trends.

## Features

- **Real-time tracking of financial news**: Get up-to-date news articles from over 60,000 sources.
- **AI-based analysis**: Leverage artificial intelligence for sentiment analysis, trend prediction, and anomaly detection.
- **Backtesting capabilities**: Explore the influence of past news on market behavior and verify your predictive models.
- **Versatile data sources**: Gain insights from a wide range of international and regional news providers.

## News Sources

AINewsTracker aggregates financial news from multiple trusted sources globally and regionally. Below is a list of these sources:



## How to use

1. Setup and activate the Python environment of your choice.
   1. `cp .env.example .env`
2. Run the following command to install the required dependencies:

```shell
# creates a virtualenv
python3.10 -m venv venv
# activates the virtualenv
source venv/bin/activate
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

## TODO

- [X] Add a new endpoint to get the news from a specific company
- [X] Implement caching to improve performance for frequently accessed data
- [ ] Add user authentication and role-based access control for secure endpoints
- [ ] Implement unit and integration testing to ensure the stability of the application
- [ ] Add pagination to news feed endpoints to limit the amount of data returned
- [X] Improve error handling and send descriptive error messages
- [X] Implement a logging system to keep track of user activity and system status
- [X] Enhance the database schema to include additional relevant fields for the articles
- [ ] Add an endpoint for users to subscribe to specific companies or news tags
- [ ] Implement a system for sending daily/weekly email updates for subscribed users
- [ ] Add multi-language support for international users
- [ ] Create a mechanism to rate-limit requests to protect the API from abuse
- [ ] Optimize database queries to improve performance
- [ ] Implement a backup system for the database
- [X] Write detailed API documentation for end-users and developers
- [X] Refactor and clean up the codebase for better maintainability
- [ ] Implement real-time updates using WebSockets
- [X] Add analytics features for tracking user behavior and system performance
