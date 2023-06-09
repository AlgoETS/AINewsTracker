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
</p>

[
    ![Open in Remote - Containers](https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode)
](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/godatadriven/python-devcontainer-template)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)


## What is AINewsTracker?

AINewsTracker is a powerful web application dedicated to backtesting the influence of financial news on the stock market. Leveraging AI to sort, filter, and analyze financial news from various reliable international and regional sources, it enables users to observe and predict potential impacts on market trends.

## How to use

1. Setup and activate the Python environment of your choice.
2. Run the following command to install the required dependencies:

```shell
pip install -r requirements.txt
```

3. Run the following command to launch FastAPI in development mode:

```shell
uvicorn app.main:app --reload
```

## Features

- **Real-time tracking of financial news**: Get up-to-date news articles from over 60,000 sources.
- **AI-based analysis**: Leverage artificial intelligence for sentiment analysis, trend prediction, and anomaly detection.
- **Backtesting capabilities**: Explore the influence of past news on market behavior and verify your predictive models.
- **Versatile data sources**: Gain insights from a wide range of international and regional news providers.

## News Sources

AINewsTracker aggregates financial news from multiple trusted sources globally and regionally. Below is a list of these sources:

## Start the application on local mode

First of all, you have to install all the dependecies :
```
pip install -r requirements.txt
```
Create a `.env` file where you copy the content of the `.env.example` file (make sure to replace the link by your own mongodb link)

Start the server with this command :
```
uvicorn app.main:app --reload
```

Then you can tryout the api by clicking [here](http://127.0.0.1:8000/docs) .


## File Structure

```shell
├── AINewsTracker.svg  # Project's logo in SVG format
├── AINewsTracker_transparent.svg  # Project's logo in SVG format with a transparent background
├── Dockerfile  # Instructions for Docker to build an image for the application
├── LICENSE  # The license of the project
├── README.md  # Overview and general documentation of the project
├── Test-AI.ipynb  # Jupyter notebook file for testing AI functionalities
├── app  # Main directory for the application source code
│   ├── __init__.py  # Python file for package initialization
│   ├── config.py  # Configuration settings for the application
│   ├── database  # Directory for database-related modules
│   │   ├── __init__.py  # Python file for package initialization
│   │   ├── config.py  # Configuration settings for the database
│   │   └── db.py  # Main database module (connection, queries, etc.)
│   ├── favicon.ico  # Favicon for the application when deployed on a web server
│   ├── main.py  # Entry point of the application
│   ├── models  # Directory for data models
│   │   ├── RSSFeed.py  # Model for RSS Feed data
│   │   ├── __init__.py  # Python file for package initialization
│   │   ├── article.py  # Model for Article data
│   │   ├── company.py  # Model for Company data
│   │   ├── score.py  # Model for Score data
│   │   └── users.py  # Model for User data
│   ├── routers  # Directory for route handlers (FastAPI)
│   │   ├── RSSFeed.py  # Route handlers for RSS Feed related operations
│   │   ├── __init__.py  # Python file for package initialization
│   │   ├── article.py  # Route handlers for Article related operations
│   │   ├── company.py  # Route handlers for Company related operations
│   │   └── users.py  # Route handlers for User related operations
│   └── services  # Directory for service functions/modules
│       ├── __init__.py  # Python file for package initialization
│       ├── article.py  # Service functions for Article related operations
│       ├── company.py  # Service functions for Company related operations
│       ├── crypto.py  # Service functions for Crypto related operations
│       ├── rss.py  # Service functions for RSS Feed related operations
│       ├── sentiments.py  # Service functions for Sentiment analysis operations
│       └── summary.py  # Service functions for Summary related operations
├── deploy  # Directory for deployment-related files
│   ├── README.md  # Deployment instructions
│   └── docker-compose.yml  # Docker Compose file for setting up the production environment
├── docker-compose.yml  # Docker Compose file for setting up the development environment
├── monitoring  # Directory for monitoring-related modules (expected to be filled with relevant files)
├── pyproject.toml  # Configuration file for Python project packaging (Poetry)
├── requirements-dev.txt  # List of Python dependencies needed in the development environment
├── requirements.txt  # List of Python dependencies needed in the production environment
├── tests  # Directory for test modules
│   ├── __init__.py  # Python file for package initialization
│   └── test_app.py  # Test cases for the application
└── wiki  # Directory for project's wiki
    ├── CODE_OF_CONDUCT.md  # Code of Conduct for project contributors
    ├── ISSUES.md  # Instructions for reporting issues
    └── WORKFLOW.md  # Guidelines for project workflow

```

## TODO

- [ ] Add a new endpoint to get the news from a specific company
